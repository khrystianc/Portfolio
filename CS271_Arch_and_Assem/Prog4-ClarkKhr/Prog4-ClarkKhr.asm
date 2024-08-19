TITLE Prime Numbers    (Prog4.asm)

;-------------------------------------------
; Author: Khrystian Clark
; Last Modified: 11/15/2020
; OSU email address: CLARKKHR@oregonstate.edu
; Course number/section:   CS271 Section 400
; Project Number:    4             Due Date: 11/15/2020
; Description: A program to calculate prime numbers from user input of how many
;              they would like to see up to 200.
;-------------------------------------------

INCLUDE Irvine32.inc
; constants
MAXNUM         =      200			; The upper and lower bounds of user input must be defined as constants.
MINNUM         =      1				; The upper and lower bounds of user input must be defined as constants.

.data
;phrases and prompts
program_name	BYTE	  "Prime Numbers",0
intro          BYTE   " Programmed by ",0 
author         BYTE   "Khrystian Clark",0
instruct1      BYTE   "Enter the number of prime numbers you would like to see.",0
instruct2      BYTE   "I accept orders for up to 200 primes.",0
getData        BYTE   "Enter the number of primes to display [1 ... 200]: ",0
invalid_err    BYTE   "No primes for you! Number out of range. Try again.",0
goodbye        BYTE   "Results certified by ",0
spaces		BYTE   "   ",0
;number and values
userNum        DWORD  ?
count          DWORD  0				; incremented in the assignment loop
primeFound     DWORD  ?
current_num    DWORD  2

.code
main PROC
;-------------------------------------------
; The main procedure must consist of only procedure calls
;-------------------------------------------
	CALL introduction
	CALL getUserData
	CALL showPrimes
	CALL farewell
	exit
main ENDP

introduction PROC
;-------------------------------------------
; The programmer’s name and program title must appear in the output.
;-------------------------------------------
	MOV  EDX, offset program_name
	CALL WriteString
	MOV  EDX, offset intro
	CALL WriteString
	MOV  EDX, offset author
	CALL WriteString
	CALL Crlf
	CALL Crlf
	MOV  EDX, offset instruct1		; Print program instructions
	CALL WriteString
	CALL Crlf
	MOV  EDX, offset instruct2
	CALL WriteString
	CALL Crlf
	CALL Crlf
	ret
introduction ENDP

getUserData PROC
;-------------------------------------------
; Procedure that takes in the user input and then calls the follow-on procedure to validate
;-------------------------------------------
	MOV  EDX, offset getData
	CALL WriteString
	CALL ReadDec
	MOV  userNum, EAX
	CALL validate
getUserData ENDP

validate PROC
;-------------------------------------------
; If the user enters a number outside the range [1 ... 200] an error message
; must be displayed and the user must be prompted to re-enter the number 
; of primes to be shown.
;-------------------------------------------
	CMP  userNum, MAXNUM
	JG   _invalid
	CMP  userNum, MINNUM
	JLE  _invalid
	CALL showPrimes

_invalid:
	MOV  EDX, offset invalid_err
	CALL WriteString
	CALL Crlf
	CALL getUserData
validate ENDP

showPrimes PROC
;-------------------------------------------
; Procedure that prints the first prime number possible, then assesses if it needs
; to continue based on the number of outpouts the user wants, if not, then is calls
; the farewell function.
;-------------------------------------------
	CALL Crlf
	MOV  EAX, 2					; Print the first prime number available
	CALL WriteDec
	MOV  EDX, offset spaces
	CALL WriteString
	CMP  userNum, MINNUM
	JLE  _done
	CALL isPrime

_done:
	CALL Crlf
	CALL farewell
showPrimes ENDP

isPrime PROC
;-------------------------------------------
; This procedure contains the counter loop, the math equations that find the continued
; primes, and prints out the next primes using the user input as the ECX counter.
;-------------------------------------------
	MOV   ECX, userNum
	DEC   ECX						; Decrement the user input since we printed the first value

_theStart:
;-------------------------------------------
; Starts the comparisons and math to find the primes without decrementing the ECX.
;-------------------------------------------
	INC   count					; Increment the counter in order to create new rows
	INC   current_num				; Increase to next possible prime number
	CDQ
	MOV   EAX, current_num
	MOV   EBX, 2					; sets/resets the EBX counter to 2
	DIV   EBX						; Divide EAX by EBX
	CMP   EDX, 0					; If remainder is 0, the number is divisible by 2, making it not prime
	JNE   _tryNext
	DEC   count
	JMP   _theStart

_nextRow:
;-------------------------------------------
; Goes to next row for input if the tenth column is reached
;-------------------------------------------
	CMP   count, 10
	JL    _theStart				; count controls keeping the 10 column limit
	MOV   count, 0
	CALL  Crlf					; or else a new row is started
	JMP   _theStart

_endIt:
;-------------------------------------------
; Jumps to the farewell procedure when the formula is out of choices
;-------------------------------------------
	CALL  Crlf
	CALL  farewell

_tryNext:
;-------------------------------------------
; Tries to divide the next EBX dec by the EAX being used
;-------------------------------------------
	INC   EBX						; Increase the tester divisor by 1 for follow-on tests
	CMP   EBX, current_num			; See if divisor is still less than possible prime
	JE    _printIt					; If EBX gets to EAX, then it proves the EAX value is prime
	CDQ
	MOV   EAX, current_num
	DIV   EBX						; Continued division with greater divisor
	CMP   EDX, 0					; If the remainder is 0 with the increased EBX, the EAX is not prime
	JE    _endIt					; If remainder is 0, the number is divisible by EBX, making it not prime
	JMP   _tryNext

_printIt:
;-------------------------------------------
; Loop function decrements the ECX counter, and goes to the farewell when the counter reaches 0
;-------------------------------------------
	MOV   EAX, current_num
	CALL  WriteDec
	MOV   EDX, offset spaces
	CALL  WriteString
	LOOP  _theStart				; See if the row has reached ten Numbers
	CALL  farewell					; Loop automatically skips when ECX is at 0, exit message

isPrime ENDP

farewell PROC
;-------------------------------------------
; The goodbye procedure containg the farewell message
;-------------------------------------------
	CALL  Crlf
	MOV   EDX, offset goodbye
	CALL  WriteString
	MOV   EDX, offset author
	CALL  WriteString
	CALL  Crlf
	
	exit
farewell ENDP
END main
