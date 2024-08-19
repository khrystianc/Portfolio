TITLE Integer Accumulator	(project3.asm)

; Author:  Khrystian Clark
; Last Modified:  11/2/2020
; OSU email address:  clarkkhr@oregonstate.edu
; Course number/section:   CS271 Section 400
; Project Number:  #3               Due Date: 11/1/2020 (used grace day)
; Description: Program that takes user input from a given range and returns the max/min values,
;			how many valid number entered, and th sum and average of the valid numbers entered.

INCLUDE Irvine32.inc

.data
;program intro
welcome		BYTE	  "Welcome to the Integer Accumulator by Khrystian Clark",0

;get the username
get_username	BYTE   "What is your name? ",0
greet_user	BYTE   "Hello there, ",0
username       BYTE   21 DUP(0)
stored_user	SDWORD ?

;give the user direction
direction1	BYTE   "Please enter numbers in [-200, -100] or [-50, -1].",0
direction2	BYTE   "Enter a non-negative number when you are finished to see results.",0

;prompt for numbers
int_val		SDWORD ?
count		SDWORD ?
accumulate	SDWORD ?
max_num		SDWORD -200
min_num		SDWORD -1
avg_nums		SDWORD ?
get_nums		BYTE   "Enter number: ",0
invalid		BYTE   "Number Invalid!",0
val1			BYTE   "You entered ",0
val2			BYTE   " valid numbers.",0
no_val		BYTE   "No valid numbers entered", 0
max_is		BYTE   "The maximum valid number is ",0
min_is		BYTE   "The minimum valid number is ",0
sum_is		BYTE   "The sum of your valid numbers is ",0
avg_is		BYTE   "The rounded average is ",0

;farewell
farewell		BYTE   "We have to stop meeting like this. Farewell, ",0


.code
main PROC
	MOV  EDX, offset welcome			; Display the program title and programmer’s name
	CALL WriteString
	CALL Crlf

	MOV  EDX, offset get_username		; Get the user's name
	CALL WriteString
	MOV  EDX, offset username
	MOV  ECX, sizeof username
	CALL ReadString
	MOV  stored_user, EAX			; Store the users name under 'username'
	CALL Crlf
	MOV  EDX, offset greet_user		; Greet the user
	CALL WriteString
	MOV  EDX, offset username
	CALL WriteString
	CALL Crlf

	MOV  EDX, offset direction1		; Display instructions for the user
	CALL WriteString
	CALL Crlf
	MOV  EDX, offset direction2
	CALL WriteString
	CALL Crlf

; Loop repeatedly prompt for user number input
_GetDigits:						; Loop to see if number input is between -100 and -200
	MOV  EDX, offset get_nums
	CALL WriteString
	CALL ReadInt
	MOV  int_val, EAX				; Assert the input at the EAX
	MOV  EBX, -200
	MOV  ECX, -100
	CMP  EAX, EBX
	JL   _InvalidNum				; if the number entered is less than -200
	CMP  EAX, ECX
	JG   _OtherRange				; if the input is greater than -100
	ADD  accumulate, EAX
	MOV  EBX, EAX
	ADD  count, 1					; Adds one to the running count
	JMP  _MakeUpdates


_OtherRange:
	;User already asked for input skip to number verification
	MOV  EBX, -50
	MOV  ECX, -1
	CMP  EAX, ECX					; Compares user input to the other range
	JG   _Display					; Goes to final operations
	CMP  EAX, EBX
	JL   _InvalidNum
	ADD  accumulate, EAX
	ADD	count, 1
	JMP  _MakeUpdates
	
_MakeUpdates:
	;Update the min and max number values
	CMP  EAX, max_num
	JG   _UpdateMax
	CMP  EAX, min_num
	JL   _UpdateMin
	JMP  _GetDigits

_UpdateMax:
	MOV  max_num, EAX
	JMP  _GetDigits

_UpdateMin:
	MOV min_num, EAX
	JMP _GetDigits

_InvalidNum:
	MOV  EDX, offset invalid			; Goes to the exit operation if the number is invalid
	CALL WriteString
	CALL Crlf
	JMP  _GetDigits

_NotNegative:
	CMP	count, 0					; Gives answers if there are numbers in the count
	JNZ  _Display
	MOV  EDX, offset no_val			; Message and goes to exit steps
	CALL WriteString
	CALL Crlf
	JMP  _TheEnd

_Display:
	;the count of the valid numbers
	MOV  EDX, offset val1
	CALL WriteString
	MOV  EAX, count
	CALL WriteDec
	MOV  EDX, offset val2
	CALL WriteString
	CALL Crlf

	;the sum of valid numbers
	MOV  EDX, offset sum_is
	CALL WriteString
	MOV  EAX, accumulate
	CALL WriteInt
	CALL Crlf

	; return the maximun valid number
	MOV  EDX, offset max_is
	CALL WriteString
	MOV  EAX, max_num
	CALL WriteInt
	CALL Crlf

	; return the minimum valid number
	MOV  EDX, offset min_is
	CALL WriteString
	MOV  EAX, min_num
	CALL WriteInt
	CALL Crlf

	; average of the entered numbers (rounded to nearest integer)
	MOV  EAX, 0
	MOV  EAX, accumulate
	CDQ
	MOV  EBX, count
	IDIV EBX							; Use the IDIV steps to find the rounded average
	MOV  EDX, offset avg_is
	CALL WriteString
	MOV  avg_nums, EAX
	CALL WriteInt
	CALL Crlf

_TheEnd:								; A parting message (with the user’s name)
	CALL Crlf
	MOV	EDX, offset farewell
	CALL WriteString
	MOV  EDX, offset username
	CALL WriteString
	

  exit
main ENDP
END MAIN

	Invoke ExitProcess,0				; exit to operating system
main ENDP


END main
