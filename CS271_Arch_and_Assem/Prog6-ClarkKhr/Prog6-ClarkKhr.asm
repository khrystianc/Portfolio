TITLE Designing low-level I/O procedures     (Prog6-ClarkKhr.asm)

; Author: Khrystian Clark  
; Last Modified: 12/8/2020
; OSU email address: CLARKKHR@oregonstate.edu
; Course number/section:   CS271 Section 400
; Project Number:     6            Due Date: 12/6/2020
; Description: This program takes on the user input of 10 signed integers and returns the integers, the sum of all integers and the average.
;              Contstraints of using macros to get and display numbers, amidst converting them from string inputs.

INCLUDE Irvine32.inc

;  constants
NUM_LO		EQU  -2147483648 ; highest and lowest possible signed integer
NUM_HI		EQU  2147483647
ARRAYSIZE		EQU  10
MAXSIZE = 11

;  macros
mGetString	MACRO	inString, strLen
			PUSH		EDX
			PUSH		ECX
			mDisplayString user_prompt
			MOV		EDX, offset inString
			MOV		ECX, MAXSIZE
			CALL		ReadString
			MOV       sLen, EAX
			POP		ECX
			POP		EDX
ENDM
mDisplayString MACRO	string
			PUSH		EDX
			MOV		EDX, offset string
			CALL      WriteString
			POP		EDX
ENDM
.data
;  Strings
intro1      BYTE  "PROGRAMMING ASSIGNMENT 6: Designing low-level I/O procedures", 0
intro2      BYTE  "Written by: Khrystian Clark", 0
prompt1     BYTE  "Please provide 10 signed decimal integers", 0
rules1      BYTE  "Each number needs to be small enough to fit inside a 32 bit register.", 0
rules2      BYTE  "After you have finished inputting the raw numbers I will display a", 0
rules3      BYTE  "list of the integers, their sum, and their average value.", 0
err_msg     BYTE  "ERROR: You did not enter a signed number or your number was too big.", 0
user_prompt BYTE  "Please enter a signed number: ", 0
num_show    BYTE  "You entered the following numbers: ", 0
comma 	  BYTE  ", ", 0
sum_show    BYTE  "The sum offset these numbers is: ", 0
avg_show    BYTE  "The rounded average is: ", 0
goodbye     BYTE  "Thanks for playing!", 0
neg_symbol  BYTE  "-", 0
; lists and variables
sLen        DWORD ?
user_input  BYTE  32  DUP(?)  
numArray    DWORD ARRAYSIZE DUP(?)   ; initialize the array of 10 elements, with no value yet
numType     DWORD TYPE numArray
arrayCount  DWORD LENGTHOF numArray  ; count of elements in the array
numByte     DWORD SIZEOF numArray    ; arrayCount x typeArray
sum         DWORD 0
avg         DWORD ?
new_num     DWORD ?                  ; placeholder for the output of writeval
counter     DWORD 0
.code
main PROC
	CALL introduction
	; convert string to integer
	PUSH sum
	PUSH offset numType	    ;32
	PUSH offset neg_symbol  ;28
	PUSH offset user_input  ;24
	PUSH offset err_msg     ;20
	PUSH offset user_prompt ;16
	PUSH DWORD counter
	PUSH offset numArray
	CALL ReadVal
	; Convert to printable digits
	PUSH offset new_num     ;32
	PUSH offset avg_show    ;28
	PUSH offset sum_show    ;24
	PUSH offset comma	    ;20
	PUSH offset num_show    ;16
	PUSH sum			    ;12
	PUSH offset numArray    ;8
	CALL WriteVal

	CALL farewell
	exit
main ENDP

; ---------------------------------------------------------------------------------
; Name: introduction
;
; Prints the programmer's name, the program title and instructions
;
; Preconditions: all variables are type BYTE. Uses Macro m DisplayString to display output
;
; Postconditions: Changes edx register. 
;
; Receives:
;		intro1,2       = string BYTE containing the program introduction
;		author		= string BYTE containing the programmer name
;		prompt1		= string BYTE containing the prompting line if instruction
;		rules1,2,3	= string BYTEs containing the lines of instruction and constraints
;
; Returns: edx			= program_name, intro, author, instructions printed out
; ---------------------------------------------------------------------------------
introduction PROC
	PUSH EBP
	MOV  EBP, ESP

	MOV  EDX, [EBP+8]
	mDisplayString EDX      ; Display title
	CALL Crlf
	MOV  EDX, [EBP+12]
	mDisplayString EDX      ; Display author
	CALL Crlf
	CALL Crlf
	MOV  EDX, [EBP+16]
	mDisplayString EDX      ; Tell the user what to do
	CALL Crlf
	MOV  EDX, [EBP+20]
	mDisplayString EDX      ; Describe contraints
	CALL Crlf
	MOV  EDX, [EBP+24]
	mDisplayString EDX
	CALL Crlf	
	MOV  EDX, [EBP+28]
	mDisplayString EDX
	CALL Crlf
	CALL Crlf

	POP  EBP
	RET  24
introduction ENDP

ReadVal PROC
	PUSH EBP
	MOV  EBP, ESP
	; receive string input
	MOV  ECX, 10				; set the outer loop counter
	MOV  EDI, [EBP+8]              ; Put the num Array in the EDI reg
get_nums:
	mGetString user_prompt, user_input
	CMP  EAX, 11
	JG   invalid_input
	MOV  ESI, [EBP+24]
	MOV	[EBP+12], EAX            ;set the inner count
	MOV  EBX, [EBP+28]
	CMP  BYTE PTR [ESI], EBX
	JE   neg_conversion
	CMP  EAX, 10
	JG   invalid_input
	JMP  conversion
	; Convert to signed integer, using LODSB/STOSB
neg_conversion:
	MOV  CH, 1                     ;set the negative flag
	INC  ESI                       ; move to the next value in the ESI
	DEC  [EBP+12]
conversion:
	MOV  AL, [ESI]
	SUB  AL, 48                    ; convert ASCII
	MOVZX EAX, AL                 ; place convert ascii digit into the EAX reg
	MOV  EBX, 10                   ; set the multiplier since were are parsing through one digit at a time
next_digit:
	INC  ESI                       ; point ESI at next digit
	DEC  [EBP+12]
	MUL  EBX
	MOV  DL, [ESI]
	SUB  DL, 48
	MOV  EDX, DL
	ADD  EAX, EDX
	CMP  [EBP+12], 0
	JG   next_digit
	JMP  check_neg
check_neg:
	CMP  CH, 1
	JNE  in_array
	NEG  EAX                       ; Make the value at EAX negative and continue to put it in the array
	; add item to array
in_array:
	MOV  [EDI], EAX
	ADD  EDI, [EBP+32]
	JMP  get_sum
	; add item to current sum
get_sum:
	ADD  [EBP+36], EAX
	CALL Crlf
	LOOP get_nums                  ; repeat loop until array has 10 elements
	; show error message
invalid_input:
	mDisplayString err_msg
	CALL Crlf
	JMP  get_nums

done:
	POP  EBP
	RET  32
ReadVal ENDP

WriteVal PROC
	PUSH EBP
	MOV  EBP, ESP
	MOV  EDI, [EBP+32]
	mDisplayString num_show
	MOV  ESI, [EBP+8]
	MOV  ECX, ARRAYSIZE
	MOV  EBX, 0
	CLD
checkNum:
	LODSB
	PUSH EAX
	ADD  [EBP+12], EAX
	MOV  EBX, 10                ; for single digit division
onebyone:
	XOR  EDX, EDX               ; clear EDX reg
	DIV  EBX
	ADD  EDX, 48                ; find ASCII value
	PUSH EDX
	TEST EAX, EAX               ; check if zero without changing the value
	JNZ  onebyone
	POP  EDX
conversion:
	STOSB
	MOV  [EBP+32], EDX          ; value of EDX in the new_num place
	mDisplayString new_num
	POP  EDX
	CMP  ESP, EBP
	JNE  conversion
	XOR  EAX, EAX
	STOSB
	ADD  EBX, EAX
	CMP  ECX, 1
	JE   nextDigit
	mDisplayString comma
nextDigit:
	LOOP checkNum
	; get the sum printed
	CALL Crlf
	mDisplayString sum_show
	MOV  EAX, [EBP+12]
	CALL WriteDec
	CALL Crlf
	; get the average printed
	mDisplayString avg_show
	CDQ
	MOV  EBX, ARRAYSIZE
	DIV  EBX
	CALL WriteDec
	CALL Crlf
finish:
	POP  EBP
	RET  12
WriteVal ENDP

farewell PROC
	CALL Crlf
	CALL Crlf
	mDisplayString goodbye
	CALL Crlf
	RET
farewell ENDP

END main