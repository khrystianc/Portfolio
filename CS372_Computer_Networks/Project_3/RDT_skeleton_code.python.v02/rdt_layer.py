from segment import Segment
import time


# #################################################################################################################### #
# RDTLayer                                                                                                             #
# Description:                                                                                                         #
# The reliable data transfer (RDT) layer is used as a communication layer to resolve issues over an unreliable         #
# channel.                                                                                                             #
# Notes:                                                                                                               #
# https://www.geeksforgeeks.org/reliable-data-transfer-rdt-3-0/
# https://www.geeksforgeeks.org/principle-of-reliable-data-transfer-protocol/
# https://www.youtube.com/watch?v=BVnmmP4BcUs
# Textbook: Ch 3.4-3.5
#
# This file is meant to be changed.                                                                                    #
# #################################################################################################################### #


class RDTLayer(object):
    # ################################################################################################################ #
    # Class Scope Variables                                                                                            #
    # ################################################################################################################ #
    DATA_LENGTH = 4  # The length of the string data sent per packet
    FLOW_CONTROL_WIN_SIZE = 15  # Receive window size for flow-control
    sendChannel = None
    receiveChannel = None
    dataToSend = ''
    currentIteration = 0  # Used for segment 'timeouts'
    
    # Add items as needed
    SENDER_WINDOW_SIZE = 5  # Desired sender window size
    RECEIVER_WINDOW_SIZE = 5  # Desired receiver window size
    TIMEOUT = 5  # Timeout value (in iterations)
    sender_window = []  # List to hold sender window segments
    receiver_window = []  # List to hold receiver window segments

    # ################################################################################################################ #
    # __init__()                                                                                                       #
    # ################################################################################################################ #
    def __init__(self):
        self.sendChannel = None
        self.receiveChannel = None
        self.dataToSend = ''
        self.currentIteration = 0
        # Add items as needed
        self.sentBuffer = dict()  # Holds record of sent segments
        self.sender_window = []  # Sender window
        self.receiver_window = []  # Receiver window
        self.terminate = False
        self.timeout_counter = 0  # Initialize the timeout counter

    # ################################################################################################################ #
    # setSendChannel()                                                                                                 #
    # Description:                                                                                                     #
    # Called by main to set the unreliable sending lower-layer channel                                                 #
    # ################################################################################################################ #
    def setSendChannel(self, channel):
        self.sendChannel = channel

    # ################################################################################################################ #
    # setReceiveChannel()                                                                                              #
    # Description:                                                                                                     #
    # Called by main to set the unreliable receiving lower-layer channel                                               #
    # ################################################################################################################ #
    def setReceiveChannel(self, channel):
        self.receiveChannel = channel

    # ################################################################################################################ #
    # setDataToSend()                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the string data to send                                                                    #
    # ################################################################################################################ #
    def setDataToSend(self,data):
        self.dataToSend = data

    # ################################################################################################################ #
    # getDataReceived()                                                                                                #
    # Description:                                                                                                     #
    # Called by main to get the currently received and buffered string data, in order                                  #
    # ################################################################################################################ #
    def getDataReceived(self):
        self.dataReceived = ''
        for i in sorted(self.sentBuffer.keys(), key=int):
            self.dataReceived += self.sentBuffer[i][0]
        return self.dataReceived

    # ################################################################################################################ #
    # processData()                                                                                                    #
    # Description:                                                                                                     #
    # "timeslice". Called by main once per iteration                                                                   #
    # ################################################################################################################ #
    def processData(self):
        self.currentIteration += 1
        self.processSend()
        self.processReceiveAndSendRespond()
        if self.dataToSend == '' and all(acknowledged for _, acknowledged in self.sentBuffer.values()):
            print('$$$$$$$$ ALL DATA SENT AND ACKNOWLEDGED $$$$$$$$')
            self.terminate = True

        print("Main--------------------------------------------")
        dataReceivedFromClient = self.getDataReceived()
        print("DataReceivedFromClient: {0}".format(dataReceivedFromClient))

    # ################################################################################################################ #
    # processSend()                                                                                                    #
    # Description:                                                                                                     #
    # Manages Segment sending tasks                                                                                    #
    # ################################################################################################################ #
    def processSend(self):
        if not self.dataToSend:
            return

        # Fill sender window with segments to send
        while len(self.sender_window) < self.SENDER_WINDOW_SIZE:
            end = min(len(self.sender_window) + self.DATA_LENGTH, len(self.dataToSend))
            segment_data = self.dataToSend[len(self.sender_window):end]

            if not segment_data:
                break

            seqnum = str(self.currentIteration)
            segmentSend = Segment()
            segmentSend.setData(seqnum, segment_data)

            # Add the timestamp when the segment is sent
            sent_time = self.currentIteration
            self.sender_window.append((segmentSend, False, sent_time))

            print("Sending segment: ", segmentSend.to_string())
            self.sendChannel.send(segmentSend)

            # Increment the timeout counter
            self.timeout_counter += 1

        self.updateSenderWindow()  # Pipeline: Continue sending more segments
        time.sleep(1)
        self.currentIteration += 1
        
    # ################################################################################################################ #
    # processReceiveAndSendRespond()                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment receive tasks and responds accordingly                                                           #
    # ################################################################################################################ #
    def processReceiveAndSendRespond(self):
        segmentAck = Segment()
        acknum = "-1"

        for incoming_segment in self.receiveChannel.receive():
            seqnum = incoming_segment.seqnum
            segment_string = incoming_segment.to_string()
            data_start = segment_string.find("data: ") + len("data: ")
            data_end = segment_string.find("\n", data_start)
            data = segment_string[data_start:data_end]

            if data:
                self.sentBuffer[seqnum] = (data, False)
                if len(self.receiver_window) < self.FLOW_CONTROL_WIN_SIZE:
                    self.receiver_window.append((incoming_segment, seqnum))
                else:
                    print("Receiver window is full, cannot accept more segments.")
            elif hasattr(incoming_segment, 'isAck') and incoming_segment.isAck():
                acknum = seqnum
                self.updateSenderWindow()

                # Filter out segments from the receiver window based on acknowledgments
                self.receiver_window = [(seg, num) for seg, num in self.receiver_window if int(num) > int(acknum)]
                self.timeout_counter = 0  # Reset the timeout counter when an acknowledgment is received

        # Check for overall timeout (optional)
        if self.timeout_counter >= self.TIMEOUT:
            print("Overall timeout reached. Retransmitting...")
            self.retransmitUnacknowledgedSegments()
            self.timeout_counter = 0  # Reset the overall timeout counter

        # Utilize cumulative acknowledgment here
        segmentAck.setAck(acknum)
        print("Sending ack: ", segmentAck.to_string())
        self.sendChannel.send(segmentAck)

    def updateSenderWindow(self):
        current_time = self.currentIteration

        for i, (segment, acknowledged, sent_time) in enumerate(self.sender_window):
            if not acknowledged and current_time - sent_time >= self.TIMEOUT:
                # Segment has timed out, retransmit it
                self.sendChannel.send(segment)
                # Update the sent_time for the retransmitted segment
                self.sender_window[i] = (segment, False, current_time)
                self.timeout_counter = 0  # Reset the timeout counter for this segment

    # Retransmit unacknowledged segments as part of Go-Back-N
    def retransmitUnacknowledgedSegments(self):
        current_time = self.currentIteration

        for i, (segment, acknowledged, sent_time) in enumerate(self.sender_window):
            if not acknowledged and current_time - sent_time >= self.TIMEOUT:
                # Segment has timed out, retransmit it
                self.sendChannel.send(segment)
                # Update the sent_time for the retransmitted segment
                self.sender_window[i] = (segment, False, current_time)