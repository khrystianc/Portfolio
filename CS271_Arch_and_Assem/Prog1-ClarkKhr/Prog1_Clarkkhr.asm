TITLE Basic Math     (Prog1_Clarkkhr.asm)

;--------------------------------------------------------------------------------------
; Author: Khrystian T Clark
; Last Modified: 10/18/2020
; OSU email address: clarkkhr@oregonstate.edu
; Course number/section:   CS271 Section 400
; Project Number:   1              Due Date: 10/18/2020
; Description: Write a program that does basic arithmetic of three numbers
;			given from user input in descending order.
;--------------------------------------------------------------------------------------

INCLUDE Irvine32.inc

.data
;  intro message and goodbye stored variables
thats_me		 BYTE  "Name: Khrystian Clark   ", 0
program_title	 BYTE  "Title: Basic Math", 0
farewell		 BYTE  "Peace Out!", 0

; equation variables and storage places
prog_desc       BYTE  "Enter 3 numbers A > B > C, in descending order, and I'll show you the sums and differences", 0
extra_cred      BYTE  "**EC: Program verifies the numbers are in descending order.", 0
enter_number_A  BYTE  "First number: ", 0
enter_number_B  BYTE  "Second number: ", 0
enter_number_C  BYTE  "Third number: ", 0
number_A        DWORD ?				;integer entered by user input
number_B        DWORD ?				;integer entered by user input
number_C        DWORD ?				;integer entered by user input

;  symbols for math
equal_sign      BYTE  " = ", 0
plus_sign       BYTE  " + ", 0
minus_sign      BYTE  " - ", 0
addition        DWORD ?
subtraction     DWORD ?

;  error message variables
lessthan        BYTE  "DESCENDING ORDER, PLEASE!", 0

.code
main PROC
	MOV  EDX, offset program_title	;  Introduces the program and the author.
	CALL WriteString
	MOV  EDX, offset thats_me
	CALL WriteString
	CALL Crlf
	CALL Crlf
	MOV  EDX, offset extra_cred		;  Displays extra credit
	CALL WriteString
	CALL Crlf
	CALL Crlf
	MOV  EDX, offset prog_desc		; Display instructions for the user
	CALL WriteString
	call Crlf
	call Crlf

	MOV  EDX, offset enter_number_A	; Prompt the user to enter three numbers (A, B, C) in descending order
	CALL WriteString
	CALL ReadInt
	MOV  number_A, EAX
	CALL Crlf

	MOV  EDX, offset enter_number_B
	CALL WriteString
	CALL ReadInt
	MOV  number_B, EAX
	CALL Crlf

	MOV	EAX, number_B				;  Make sure A and B are in descending order
	CMP	EAX, number_A				;  Compares the two initial numbers
	JG	_ErrorMessage				;  Returns the error message and ends rthe program
	JLE	_NumberC					;  Moves to the next number input

_NumberC:
	MOV  EDX, offset enter_number_C	;  Prompts user for the third number if A and B are in descending order
	CALL WriteString
	CALL ReadInt
	MOV  number_C, EAX
	CALL Crlf

	;compare B and C to ensure descending order
	MOV  EAX, number_C
	CMP  EAX, number_B
	JG   _ErrorMessage				;  Returns the error message and ends the program.
	JLE  _DoTheMath				;  Moves to the equations for the three numbers.


_DoTheMath:						;  the equations and print outs of each promised equation.

	; A+B
	MOV  EAX, number_A
	ADD  EAX, number_B
	MOV  addition, EAX				;  Adds the first two numbers
	MOV  EAX, number_A
	CALL WriteDec
	MOV  EDX, offset plus_sign
	CALL WriteString
	MOV  EAX, number_B
	CALL WriteDec
	MOV  EDX, offset equal_sign
	CALL WriteString
	MOV  EAX, addition
	CALL WriteDec
	CALL CRLF

	; A-B
	MOV  EAX, number_A
	SUB  EAX, number_B
	MOV  subtraction, EAX			;  Subtracts the second number from the first
	MOV  EAX, number_A
	CALL WriteDec
	MOV  EDX, offset minus_sign
	CALL WriteString
	MOV  EAX, number_B
	CALL WriteDec
	MOV  EDX, offset equal_sign
	CALL WriteString
	MOV  EAX, subtraction
	CALL WriteDec
	CALL CRLF

	; A+C
	MOV	EAX, number_A
	ADD	EAX, number_C
	MOV	addition, EAX				;  Adds the first number and third number
	MOV	EAX, number_A
	CALL WriteDec
	MOV	EDX, offset plus_sign
	CALL WriteString
	MOV	EAX, number_C
	CALL WriteDec
	MOV	EDX, offset equal_sign
	CALL WriteString
	MOV	EAX, addition
	CALL WriteDec
	CALL CRLF

	; A-C
	MOV	EAX, number_A
	SUB	EAX, number_C
	MOV	subtraction, EAX			;  Subtracts third number from first number
	MOV	EAX, number_A
	CALL WriteDec
	MOV	EDX, offset minus_sign
	CALL WriteString
	MOV	EAX, number_C
	CALL WriteDec
	MOV	EDX, offset equal_sign
	CALL WriteString
	MOV	EAX, subtraction
	CALL WriteDec
	CALL CRLF

	; B+C
	MOV	EAX, number_B
	ADD	EAX, number_C
	MOV	addition, EAX				;  Adds the second and third number
	MOV	EAX, number_B
	CALL WriteDec
	MOV	EDX, offset plus_sign
	CALL WriteString
	MOV	EAX, number_C
	CALL WriteDec
	MOV	EDX, offset equal_sign
	CALL WriteString
	MOV	EAX, addition
	CALL WriteDec
	CALL	CRLF

	; B-C
	MOV	EAX, number_B
	SUB	EAX, number_C
	MOV	subtraction, EAX			;  Subtracts the third number from the second number
	MOV	EAX, number_B
	CALL WriteDec
	MOV	EDX, offset minus_sign
	CALL WriteString
	MOV	EAX, number_C
	CALL WriteDec
	MOV	EDX, offset equal_sign
	CALL WriteString
	MOV	EAX, subtraction
	CALL WriteDec
	CALL CRLF

	; A+B+C
	MOV	EAX, number_A
	ADD	EAX, number_B
	ADD	EAX, number_C
	MOV	addition, EAX				;  Adds all three integers given
	MOV  EAX, number_A
	CALL WriteDec
	MOV	EDX, offset plus_sign
	CALL WriteString
	MOV	EAX, number_B
	CALL WriteDec
	MOV	EDX, offset plus_sign
	CALL WriteString
	MOV	EAX, number_C
	CALL WriteDec
	MOV	EDX, offset equal_sign
	CALL WriteString
	MOV	EAX, addition
	CALL WriteDec
	CALL CRLF
	CALL Crlf
	JG	_TheEnd

_ErrorMessage: 
	; error message that only occurs when called
	MOV	EDX, offset lessthan		;  Error message returned if the numbers are not in descending order
	CALL WriteString
	CALL Crlf
	JG	_TheEnd					;  Takes the user to the end/end message of the program for various reasons.

_TheEnd:
	; Display a closing message end exit 
	MOV	EDX, offset farewell
	CALL WriteString
	CALL Crlf

	exit	; exit to operating system
main ENDP
END main