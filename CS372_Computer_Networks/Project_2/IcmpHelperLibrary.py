# Imports necessary modules
import os
from socket import *
import struct
import time
import select


# Class IcmpHelperLibrary                                                                                              #
class IcmpHelperLibrary:
    ICMP_ERROR_CODES = { # Add as many ICMP error codes thta you think till come up
                (0, 0): "Echo Reply",
                (3, 0): "Destination Network Unreachable",
                (3, 1): "Destination Host Unreachable",
                (3, 2): "Destination Protocol Unreachable",
                (3, 3): "Destination Port Unreachable",
                (3, 4): "Fragmentation required, and DF flag set",
                (3, 5): "Source route failed",
                (3, 6): "Destination network unknown",
                (3, 7): "Destination host unknown",
                (3, 8): "Source host isolated",
                (3, 9): "Network administratively prohibited",
                (3, 10): "Host administratively prohibited",
                (3, 11): "Network unreachable for ToS",
                (3, 12): "Host unreachable for ToS",
                (3, 13): "Communication administratively prohibited",
                (3, 14): "Host Precedence Violation",
                (3, 15): "Precedence cutoff in effect",
                (11, 0): "Time to live exceeded in transit",
                (11, 1): "Fragment reassembly time exceeded"
            }

    # Class IcmpPacket
    class IcmpPacket:
        # IcmpPacket Class Scope Variables to construct ICMP packet
        __icmpTarget = ""               # Remote Host
        __destinationIpAddress = ""     # Remote Host IP Address
        __header = b''                  # Header after byte packing
        __data = b''                    # Data after encoding
        __dataRaw = ""                  # Raw string data before encoding
        __icmpType = 0                  # Valid values are 0-255 (unsigned int, 8 bits)
        __icmpCode = 0                  # Valid values are 0-255 (unsigned int, 8 bits)
        __packetChecksum = 0            # Valid values are 0-65535 (unsigned short, 16 bits)
        __packetIdentifier = 0          # Valid values are 0-65535 (unsigned short, 16 bits)
        __packetSequenceNumber = 0      # Valid values are 0-65535 (unsigned short, 16 bits)
        __ipTimeout = 30
        __ttl = 255                     # Time to live
        __DEBUG_IcmpPacket = False      # Allows for debug output

        # Added this line to initialize __recvSocket 
        __recvSocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)

        __DEBUG_IcmpPacket = False      # Allows for debug output

        # IcmpPacket Class Getters
        def getIcmpTarget(self):
            return self.__icmpTarget
        def getDataRaw(self):
            return self.__dataRaw
        def getIcmpType(self):
            return self.__icmpType
        def getIcmpCode(self):
            return self.__icmpCode
        def getPacketChecksum(self):
            return self.__packetChecksum
        def getPacketIdentifier(self):
            return self.__packetIdentifier
        def getPacketSequenceNumber(self):
            return self.__packetSequenceNumber
        def getTtl(self):
            return self.__ttl

        # IcmpPacket Class Setters
        def setIcmpTarget(self, icmpTarget):
            self.__icmpTarget = icmpTarget
            # Only get destination address if it is not empty
            if len(self.__icmpTarget.strip()) > 0:
                self.__destinationIpAddress = gethostbyname(self.__icmpTarget.strip())
        def setIcmpType(self, icmpType):
            self.__icmpType = icmpType
        def setIcmpCode(self, icmpCode):
            self.__icmpCode = icmpCode
        def setPacketChecksum(self, packetChecksum):
            self.__packetChecksum = packetChecksum
        def setPacketIdentifier(self, packetIdentifier):
            self.__packetIdentifier = packetIdentifier
        def setPacketSequenceNumber(self, sequenceNumber):
            self.__packetSequenceNumber = sequenceNumber
        def setTtl(self, ttl):
            self.__ttl = ttl

        # IcmpPacket Class Private Functions
        def __recalculateChecksum(self):
            print("calculateChecksum Started...") if self.__DEBUG_IcmpPacket else 0
            packetAsByteData = b''.join([self.__header, self.__data])
            checksum = 0
            # This checksum function will work with pairs of values with two separate 16 bit segments. Any remaining
            # 16 bit segment will be handled on the upper end of the 32 bit segment.
            countTo = (len(packetAsByteData) // 2) * 2
            # Calculate checksum for all paired segments
            print(f'{"Count":10} {"Value":10} {"Sum":10}') if self.__DEBUG_IcmpPacket else 0
            count = 0
            while count < countTo:
                thisVal = packetAsByteData[count + 1] * 256 + packetAsByteData[count]
                checksum = checksum + thisVal
                checksum = checksum & 0xffffffff        # Capture 16 bit checksum as 32 bit value
                print(f'{count:10} {hex(thisVal):10} {hex(checksum):10}') if self.__DEBUG_IcmpPacket else 0
                count = count + 2
            # Calculate checksum for remaining segment (if there are any)
            if countTo < len(packetAsByteData):
                thisVal = packetAsByteData[len(packetAsByteData) - 1]
                checksum = checksum + thisVal
                checksum = checksum & 0xffffffff        # Capture as 32 bit value
                print(count, "\t", hex(thisVal), "\t", hex(checksum)) if self.__DEBUG_IcmpPacket else 0
            # Add 1's Complement Rotation to original checksum
            checksum = (checksum >> 16) + (checksum & 0xffff)   # Rotate and add to base 16 bits
            checksum = (checksum >> 16) + checksum              # Rotate and add
            answer = ~checksum                  # Invert bits
            answer = answer & 0xffff            # Trim to 16 bit value
            answer = answer >> 8 | (answer << 8 & 0xff00)
            print("Checksum: ", hex(answer)) if self.__DEBUG_IcmpPacket else 0
            self.setPacketChecksum(answer)
        def __packHeader(self):
            # The following header is based on http://www.networksorcery.com/enp/protocol/icmp/msg8.htm
            # Type = 8 bits
            # Code = 8 bits
            # ICMP Header Checksum = 16 bits
            # Identifier = 16 bits
            # Sequence Number = 16 bits
            self.__header = struct.pack("!BBHHH",
                                   self.getIcmpType(),              #  8 bits / 1 byte  / Format code B
                                   self.getIcmpCode(),              #  8 bits / 1 byte  / Format code B
                                   self.getPacketChecksum(),        # 16 bits / 2 bytes / Format code H
                                   self.getPacketIdentifier(),      # 16 bits / 2 bytes / Format code H
                                   self.getPacketSequenceNumber()   # 16 bits / 2 bytes / Format code H
                                   )
        def __encodeData(self):
            data_time = struct.pack("d", time.time())               # Used to track overall round trip time
                                                                    # time.time() creates a 64 bit value of 8 bytes
            dataRawEncoded = self.getDataRaw().encode("utf-8")
            self.__data = data_time + dataRawEncoded
        def __packAndRecalculateChecksum(self):
            # Checksum is calculated with the following sequence to confirm data in up to date
            self.__packHeader()                 # packHeader() and encodeData() transfer data to their respective bit
                                                # locations, otherwise, the bit sequences are empty or incorrect.
            self.__encodeData()
            self.__recalculateChecksum()        # Result will set new checksum value
            self.__packHeader()                 # Header is rebuilt to include new checksum value

        def __validateIcmpReplyPacketWithOriginalPingData(self, icmpReplyPacket):
            # Confirm the following items received are the same as what was sent: sequence number, packet identifier, raw data
            # Get the original values
            original_sequence_number = self.getPacketSequenceNumber()
            original_packet_identifier = self.getPacketIdentifier()
            original_raw_data = self.getDataRaw()

            # Extract the values from the received ICMP echo reply
            received_sequence_number = icmpReplyPacket.getIcmpSequenceNumber()
            received_packet_identifier = icmpReplyPacket.getIcmpIdentifier()
            received_raw_data = icmpReplyPacket.getIcmpData()

            # Initialize all checks as false
            identifier_check = sequence_check = data_check = False

            # Compare the received values with the original ones and set the validity
            if received_packet_identifier == original_packet_identifier:
                identifier_check = True
                icmpReplyPacket.setIcmpIdentifier_isValid(True)

            if received_sequence_number == original_sequence_number:
                sequence_check = True
                icmpReplyPacket.setIcmpSequenceNumber_isValid(True)

            if received_raw_data == original_raw_data:
                data_check = True
                icmpReplyPacket.setIcmpData_isValid(True)  # Assuming you have added this method

            # Set overall response validity
            overall_validity = identifier_check and sequence_check and data_check
            icmpReplyPacket.setIsValidResponse(overall_validity)

            # Print the validation result
            if not overall_validity:
                if not identifier_check:
                    print("Validation failed for Identifier.")
                    print(f"Expected Identifier: {original_packet_identifier}, Received Identifier: {received_packet_identifier}")
                if not sequence_check:
                    print("Validation failed for Sequence Number.")
                    print(f"Expected Sequence Number: {original_sequence_number}, Received Sequence Number: {received_sequence_number}")
                if not data_check:
                    print("Validation failed for Data.")
                    print(f"Expected Data: {original_raw_data}, Received Data: {received_raw_data}")
                return False
            else:
                print("Validation successful. All values match.")
                return True
            
        # IcmpPacket Class Public Functions
        def buildPacket_echoRequest(self, packetIdentifier, packetSequenceNumber):
            self.setIcmpType(8)
            self.setIcmpCode(0)
            self.setPacketIdentifier(packetIdentifier)
            self.setPacketSequenceNumber(packetSequenceNumber)
            self.__dataRaw = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            self.__packAndRecalculateChecksum()
        def sendEchoRequest(self):
            # Logic adapted from common ICMP ping functions found on Stack Overflow
            # If ICMP target or destination IP address is not provided, use default values
            if not self.__icmpTarget.strip() or not self.__destinationIpAddress.strip():
                self.setIcmpTarget("127.0.0.1")

            # Print the target and destination IP address
            print("Pinging (" + self.__icmpTarget + ") " + self.__destinationIpAddress)

            # Create a raw socket to send and receive ICMP packets
            mySocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
            mySocket.settimeout(self.__ipTimeout)
            mySocket.bind(("", 0))
            mySocket.setsockopt(IPPROTO_IP, IP_TTL, struct.pack('B', self.getTtl()))  # Use 'B' for a single-byte integer
            try:
                # Send the ICMP echo request packet
                mySocket.sendto(b''.join([self.__header, self.__data]), (self.__destinationIpAddress, 0))
                timeLeft = 30
                pingStartTime = time.time()
                startedSelect = time.time()
                whatReady = select.select([mySocket], [], [], timeLeft)
                endSelect = time.time()
                howLongInSelect = (endSelect - startedSelect)
                if whatReady[0] == []:  # Timeout
                    print("  *        *        *        *        *    Request timed out.")
                recvPacket, addr = mySocket.recvfrom(1024)  # recvPacket - bytes object representing data received
                # addr  - address of socket sending data
                timeReceived = time.time()
                timeLeft = timeLeft - howLongInSelect
                if timeLeft <= 0:
                    print("  *        *        *        *        *    Request timed out (By no remaining time left).")

                else:
                    # Fetch the ICMP type and code from the received packet
                    icmpType, icmpCode = recvPacket[20:22]

                    # Check ICMP response error codes
                    icmp_errors = IcmpHelperLibrary.ICMP_ERROR_CODES
                    error_message = icmp_errors.get((icmpType, icmpCode), "Unknown Error")

                    if icmpType == 11:  # Time Exceeded
                        print("  TTL=%d    RTT=%.0f ms    Type=%d    Code=%d    %s" %
                                (
                                    self.getTtl(),
                                    (timeReceived - pingStartTime) * 1000,
                                    icmpType,
                                    icmpCode,
                                    addr[0]
                                )
                            )
                        print(f"ICMP Error: {error_message}")

                    elif icmpType == 3:  # Destination Unreachable
                        print("  TTL=%d    RTT=%.0f ms    Type=%d    Code=%d    %s" %
                                (
                                    self.getTtl(),
                                    (timeReceived - pingStartTime) * 1000,
                                    icmpType,
                                    icmpCode,
                                    addr[0]
                                )
                            )
                        print(f"ICMP Error: {error_message}")

                    elif icmpType == 0:  # Echo Reply
                        icmpReplyPacket = IcmpHelperLibrary.IcmpPacket_EchoReply(recvPacket)
                        self.__validateIcmpReplyPacketWithOriginalPingData(icmpReplyPacket)
                        icmpReplyPacket.printResultToConsole(self.getTtl(), timeReceived, addr)
                        return  # Echo reply is the end and therefore should return

                    else:
                        print("error")
            except timeout:
                print("  *        *        *        *        *    Request timed out (By Exception).")
            finally:
                mySocket.close()  

        def printIcmpPacketHeader_hex(self):
            print("Header Size: ", len(self.__header))
            for i in range(len(self.__header)):
                print("i=", i, " --> ", self.__header[i:i+1].hex())
        def printIcmpPacketData_hex(self):
            print("Data Size: ", len(self.__data))
            for i in range(len(self.__data)):
                print("i=", i, " --> ", self.__data[i:i + 1].hex())
        def printIcmpPacket_hex(self):
            print("Printing packet in hex...")
            self.printIcmpPacketHeader_hex()
            self.printIcmpPacketData_hex()
        def getEchoReply(self):
            # Receive the ping reply
            timeReceived = time.time()

            try:
                packet_data, addr = self.__recvSocket.recvfrom(1024)
            except timeout:
                print("  *        *        *        *        *    Request timed out (By Exception).")
                return None, True
            except KeyboardInterrupt:
                print("Ping request interrupted.")
                return None, True
            except Exception as e:
                print(f"Error receiving ICMP echo reply: {e}")
                return None, True
            
            # Create an IcmpPacket_EchoReply object
            icmpEchoReply = IcmpHelperLibrary.IcmpPacket_EchoReply(packet_data)

            # Validate the echo reply packet
            self.__validateIcmpReplyPacketWithOriginalPingData(icmpEchoReply)

            # Check the ICMP type and code
            icmp_type, icmp_code = icmpEchoReply.getIcmpType(), icmpEchoReply.getIcmpCode()

            # Define a dictionary of ICMP error codes and messages
            icmp_errors = self.ICMP_ERROR_CODES.get((self.icmpType, self.icmpCode), "Unknown Error")

            # Check if the ICMP type and code are in the "dictionary"
            if (icmp_type, icmp_code) in icmp_errors:
                # Display the corresponding error message
                error_message = icmp_errors[(icmp_type, icmp_code)]
                print(f"ICMP Error: {error_message}")
            else:
                # Display an unknown error message
                print(f"ICMP Error: Unknown type {icmp_type} and code {icmp_code}")

            # Return the time received and the packet loss flag
            return timeReceived, not icmpEchoReply.isValidResponse()
        def isTargetReached(self):
            # Implement logic here to check if the target host is reached
            # You can use the information gathered during the traceroute
            # For example, if you receive an ICMP Echo Reply (Type 0) from the target host, consider it reached.
            return self.getIcmpType() == 0  # Replace with your specific logic

    # Class IcmpPacket_EchoReply                                                                                       #
    # References:                                                                                                      #
    # http://www.networksorcery.com/enp/protocol/icmp/msg0.htm                                                         #
    class IcmpPacket_EchoReply:
        # IcmpPacket_EchoReply Class Scope Variables to receive ICMP reply packets
        __recvPacket = b''
        __isValidResponse = False

        # IcmpPacket_EchoReply Constructors to track validity of the values                                                                          #
        def __init__(self, recvPacket):
            self.__recvPacket = recvPacket
            self.__icmpType_isValid = False
            self.__icmpCode_isValid = False
            self.__icmpHeaderChecksum_isValid = False
            self.__icmpIdentifier_isValid = False
            self.__icmpSequenceNumber_isValid = False
            self.__dateTimeSent_isValid = False

        # IcmpPacket_EchoReply Getters and Setters
        def getIcmpType(self):
            return self.__unpackByFormatAndPosition("B", 20)
        def getIcmpType_isValid(self):
            return self.__icmpType_isValid
        def setIcmpType_isValid(self, isValid):
            self.__icmpType_isValid = isValid

        def getIcmpCode(self):
            return self.__unpackByFormatAndPosition("B", 21)
        def getIcmpCode_isValid(self):
            return self.__icmpCode_isValid
        def setIcmpCode_isValid(self, isValid):
            self.__icmpCode_isValid = isValid

        def getIcmpHeaderChecksum(self):
            return self.__unpackByFormatAndPosition("H", 22)
        def getIcmpHeaderChecksum_isValid(self):
            return self.__icmpHeaderChecksum_isValid
        def setIcmpHeaderChecksum_isValid(self, isValid):
            self.__icmpHeaderChecksum_isValid = isValid

        def getIcmpIdentifier(self):
            return self.__icmpIdentifier_isValid, self.__unpackByFormatAndPosition("H", 24)
        def getIcmpIdentifier_isValid(self):
            return self.__icmpIdentifier_isValid
        def setIcmpIdentifier_isValid(self, isValid):
            self.__icmpIdentifier_isValid = isValid

        def getIcmpSequenceNumber(self):
            return self.__unpackByFormatAndPosition("H", 26)
        def getIcmpSequenceNumber_isValid(self):
            return self.__icmpSequenceNumber_isValid
        def setIcmpSequenceNumber_isValid(self, isValid):
            self.__icmpSequenceNumber_isValid = isValid

        def getDateTimeSent(self):
            # This accounts for bytes 28 through 35 = 64 bits
            return self.__unpackByFormatAndPosition("d", 28)   # Used to track overall round trip time
        def getDateTimeSent_isValid(self):
            return self.__dateTimeSent_isValid
        def setDateTimeSent_isValid(self, isValid):
            self.__dateTimeSent_isValid = isValid

        def getIcmpData(self):
            # This accounts for bytes 36 to the end of the packet.
            return self.__recvPacket[36:].decode('utf-8')
        def getIcmpData_isValid(self):
            return self.__icmpData_isValid
        def setIcmpData_isValid(self, isValid):
            self.__icmpData_isValid = isValid

        def isValidResponse(self):
            return self.__isValidResponse

        # IcmpPacket_EchoReply Setters                                                                                 #
        def setIsValidResponse(self, booleanValue):
            self.__isValidResponse = booleanValue

        # IcmpPacket_EchoReply Private Functions                                                                       #
        def __unpackByFormatAndPosition(self, formatCode, basePosition):
            numberOfbytes = struct.calcsize(formatCode)
            return struct.unpack("!" + formatCode, self.__recvPacket[basePosition:basePosition + numberOfbytes])[0]

        # IcmpPacket_EchoReply Public Functions                                                                        #
        def printResultToConsole(self, ttl, timeReceived, addr):
            bytes = struct.calcsize("d")
            timeSent = struct.unpack("d", self.__recvPacket[28:28 + bytes])[0]

            expected_identifier = self.getIcmpIdentifier()  # Get the expected Identifier from the packet
            expected_sequence_number = self.getIcmpSequenceNumber()  # Get the expected Sequence Number from the packet

            received_identifier = struct.unpack("H", self.__recvPacket[36:38])[0]  # Extract the received Identifier
            received_sequence_number = struct.unpack("H", self.__recvPacket[38:40])[0]  # Extract the received Sequence Number

            if expected_identifier != received_identifier:
                print(f"Error: Expected Identifier={expected_identifier}, Received Identifier={received_identifier}")
            
            if expected_sequence_number != received_sequence_number:
                print(f"Error: Expected Sequence Number={expected_sequence_number}, Received Sequence Number={received_sequence_number}")

            print("TTL=%d    RTT=%.0f ms    Type=%d    Code=%d        Identifier=%d    Sequence Number=%d    %s" %
                (
                    ttl,
                    (timeReceived - timeSent) * 1000,
                    self.getIcmpType(),
                    self.getIcmpCode(),
                    received_identifier,  # Print the received Identifier
                    received_sequence_number,  # Print the received Sequence Number
                    addr[0]
                )
                )
    
    # Class IcmpHelperLibrary                                                                                          #
    # IcmpHelperLibrary Class Scope Variables                                                                          #
    __DEBUG_IcmpHelperLibrary = False                  # Allows for debug output

    # IcmpHelperLibrary Private Functions                                                                              #
    def __sendIcmpEchoRequest(self, host):
        print("sendIcmpEchoRequest Started...") if self.__DEBUG_IcmpHelperLibrary else 0
        
        # Send 4 ICMP Echo Requests in a loop
        for i in range(4):
            # Build ICMP packet
            icmpPacket = IcmpHelperLibrary.IcmpPacket()

            # Generate a random 16-bit identifier for the ICMP packet
            randomIdentifier = (os.getpid() & 0xffff)      # Get as 16 bit number - Limit based on ICMP header standards

            # Set packetIdentifier and packetSequenceNumber
            packetIdentifier = randomIdentifier
            packetSequenceNumber = i

            # Build the ICMP Echo Request packet
            icmpPacket.buildPacket_echoRequest(packetIdentifier, packetSequenceNumber)  # Build ICMP for IP payload
            icmpPacket.setIcmpTarget(host)
            icmpPacket.sendEchoRequest()                                                # Build IP

            icmpPacket.printIcmpPacketHeader_hex() if self.__DEBUG_IcmpHelperLibrary else 0
            icmpPacket.printIcmpPacket_hex() if self.__DEBUG_IcmpHelperLibrary else 0
            # we should be confirming values are correct, such as identifier and sequence number and data

    def __sendIcmpTraceRoute(self, host):
        print("TraceRoute to " + host + " Started...") if self.__DEBUG_IcmpHelperLibrary else 0
        
        # Define the maximum number of hops for the TraceRoute
        max_hops = 30

        # Iterate through TTL values from 1 to the maximum number of hops
        for ttl in range(1, max_hops + 1):
            # Create an ICMP packet for sending Echo Requests
            icmpPacket = IcmpHelperLibrary.IcmpPacket()

            # Generate a random identifier for the ICMP packet (16-bit)
            randomIdentifier = (os.getpid() & 0xffff)

            # Set the packet's identifier and sequence number based on the TTL
            packetIdentifier = randomIdentifier
            packetSequenceNumber = ttl

            # Build the ICMP Echo Request packet
            icmpPacket.buildPacket_echoRequest(packetIdentifier, packetSequenceNumber)
            
            # Set the target host and TTL in the ICMP packet
            icmpPacket.setIcmpTarget(host)
            icmpPacket.setTtl(ttl)

            # Time when the Echo Request is sent
            send_time = time.time()
            icmpPacket.sendEchoRequest()
            receive_time, packet_loss = icmpPacket.getEchoReply()

            if packet_loss:
                print(f"{ttl}: *")
            else:
                rtt = (receive_time - send_time) * 1000
                print(f"{ttl}: {host} {rtt:.2f} ms")
            # Check if the target host is reached, and if so, exit the loop
            if icmpPacket.isTargetReached():
                print(f"TraceRoute to {host} completed.")
                break
    
    # IcmpHelperLibrary Public Functions                                                                               #
    def sendPing(self, targetHost, ping_count=4):
        # Send ICMP echo requests to a specified host, calculate round-trip time stats
        print(f"Pinging ({targetHost})")
        rtt_values = []
        lost_packets = 0
        icmp_type_3_count = 0
        icmp_type_11_count = 0

        min_rtt = float('inf')  # Initialize min_rtt with a high value
        max_rtt = 0
        total_rtt = 0

        for i in range(ping_count):
            icmpPacket = IcmpHelperLibrary.IcmpPacket()
            randomIdentifier = (os.getpid() & 0xffff)
            packetIdentifier = randomIdentifier
            packetSequenceNumber = i

            icmpPacket.buildPacket_echoRequest(packetIdentifier, packetSequenceNumber)
            icmpPacket.setIcmpTarget(targetHost)

            # Record the time before sending the packet
            send_time = time.time()

            try:
                icmpPacket.sendEchoRequest()

                # Record the time after receiving the packet and check for packet loss
                receive_time, addr = icmpPacket.getEchoReply()

                if receive_time is not None and send_time is not None:
                    # Calculate and store round-trip time (RTT)
                    rtt = (receive_time - send_time) * 1000
                    rtt_values.append(rtt)

                    # Update min_rtt, max_rtt, and total_rtt
                    min_rtt = min(min_rtt, rtt)
                    max_rtt = max(max_rtt, rtt)
                    total_rtt += rtt

                    # Check if it's a type 3 (Destination Unreachable) or type 11 (Time Exceeded) ICMP response
                    icmp_type, icmp_code = icmpPacket.getIcmpType()

                    if icmp_type == 3:
                        icmp_type_3_count += 1
                        print(f"Type 3 (Destination Unreachable) ICMP Response Received. Code: {icmp_code}")
                    elif icmp_type == 11:
                        icmp_type_11_count += 1
                        print(f"Type 11 (Time Exceeded) ICMP Response Received. Code: {icmp_code}")

                    print(f"Reply from {targetHost}: time={rtt:.2f}ms, Type={icmp_type}, Code={icmp_code}")
                else:
                    # Handle the case where send_time or receive_time is None
                    print("Error: send_time or receive_time is None")
            except TimeoutError:
                # Handle timeout
                lost_packets += 1
                print("Request timed out.")
        # Display summary statistics
        print("\n--- Ping statistics for {} ---".format(targetHost))
        print(f"Packets: Sent = {ping_count}, Received = {ping_count - lost_packets}, Lost = {lost_packets} ({(lost_packets / ping_count) * 100:.2f}% loss)")

        if rtt_values:
            # Calculate and display RTT statistics
            avg_rtt = total_rtt / len(rtt_values)
            packet_loss_rate = (lost_packets / ping_count) * 100

            print("\nPing statistics for", targetHost)
            print(f"    Packets: Sent = {ping_count}, Received = {ping_count - lost_packets}, Lost = {lost_packets} ({packet_loss_rate:.2f}% loss)")
            print(f"    Type 3 (Destination Unreachable) ICMP Responses: {icmp_type_3_count} received")
            print(f"    Type 11 (Time Exceeded) ICMP Responses: {icmp_type_11_count} received")
            print("Approximate round trip times in milliseconds:")
            print(f"    Minimum = {min_rtt:.2f}ms, Maximum = {max_rtt:.2f}ms, Average = {avg_rtt:.2f}ms")
    
    def traceRoute(self, targetHost):
        # Perform traceroute to the target host
        print("traceRoute Started...") if self.__DEBUG_IcmpHelperLibrary else 0
        self.__sendIcmpTraceRoute(targetHost)


# main()                                                                                                               #
def main():
    icmpHelperPing = IcmpHelperLibrary()


    # Choose ONE of the following by uncommenting out the line
    # icmpHelperPing.sendPing("209.233.126.254")
    # icmpHelperPing.sendPing("www.google.com")
    # icmpHelperPing.sendPing("gaia.cs.umass.edu")
    # icmpHelperPing.traceRoute("164.151.129.20")
    # icmpHelperPing.traceRoute("122.56.99.243")
    # icmpHelperPing.traceRoute("www.govt.uk")
    icmpHelperPing.traceRoute("www.govt.nz")


if __name__ == "__main__":
    main()
