TITLE Generating, Sorting, and Counting Random integers!     (Prog5-ClarkKhr.asm)

; Author: Khrystian Clark
; Last Modified: 11/19/2020
; OSU email address: ClarkKhr@oregonstate.edu
; Course number/section:   CS271 Section 400
; Project Number:       Program 5          Due Date: 11/22/2020
; Description: This program produces a randomized list of 200 values
;              Returns the list, the median, sorted list and the counts of repeat instances.

INCLUDE Irvine32.inc
; Constants: Low and Hi range of random values to generate
LO = 10
HI = 29
ARRAYSIZE = 200
ROW_LIMIT = 20

.data
intro1   BYTE "Generating, Sorting, and Counting Random integers! Programmed by Khrystian Clark",0
intro2   BYTE "This program generates 200 random number in the reange [10...29]. Actions: Sorts the list, finds the median, counts repeats, Returns: original list, median value, sorted list, number offset instances offset repeated values.",0
showUns  BYTE "Your unsorted random numbers:",0
showMed  BYTE "The median value of the array: ",0
showSort BYTE "Your sorted random numbers:",0
showInst BYTE "Your list of instances of each generated number, starting with the number of 10s:",0
goodbye  BYTE "Goodbye, and thanks for using this program!",0
spaces   BYTE "  ",0

someArray DWORD ARRAYSIZE DUP(?)
newArray  DWORD ARRAYSIZE DUP(?)
lastArray DWORD ARRAYSIZE DUP(?)
counts    DWORD 20        DUP(?)

.code
main PROC
	CALL Randomize        ; Call Randomize once at the beginning of the program
	; introduction
	PUSH offset intro1    ; Word (12)
	PUSH offset intro2    ; Word (8)
	CALL introduction
	; fillArray
	PUSH HI		       ; value. 20
	PUSH LO			  ; value. 16
	PUSH ARRAYSIZE		  ; value. 12
	PUSH offset someArray ; DWORD, 8 bytes
	CALL fillArray
	; display original list
	PUSH offset spaces    ; 20
	PUSH offset someArray ; 16
	PUSH offset showUns   ; 12
	PUSH ARRAYSIZE		  ; 8
	CALL displayList
	; sortList
	PUSH ARRAYSIZE        ; value. 12
	PUSH offset someArray ; ref, 8
	CALL sortList
	; display the median
	PUSH ARRAYSIZE		  ; 16
	PUSH offset someArray ; 12
	PUSH offset showMed   ; 8
	CALL displayMedian
	; display sorted list
	PUSH offset spaces    ; 20
	PUSH offset someArray ; 16
	PUSH offset showSort  ; 12
	PUSH ARRAYSIZE        ; 8
	CALL displayList
	; PUSH offset someArray1
	PUSH offset counts    ; 24
	PUSH offset someArray ; 20
	PUSH ARRAYSIZE        ; 16
	PUSH LO               ; 12
	PUSH HI			  ; 8
	CALL countList
	; display count array
	PUSH offset spaces    ; 20
	PUSH offset someArray ; 16
	PUSH offset showInst  ; 12
	PUSH ARRAYSIZE		  ; 8
	CALL displayList
	; done
	PUSH offset goodbye   ; 8
	CALL farewell
	exit
main ENDP
introduction PROC
; offset intro1  12
; offset intro2  8
	PUSH EBP
	MOV  EBP, ESP
	MOV  EDX, [EBP+12]
	CALL WriteString
	CALL Crlf
	CALL Crlf
	MOV  EDX, [EBP+8]
	CALL WriteString
	CALL Crlf

	POP  EBP
	RET  12
introduction ENDP
fillArray PROC
; parameters: someArray (reference, output), LO (value, input), HI (value, input), ARRAYSIZE (value, input)
; HI		          20
; LO			     16
; ARRAYSIZE		12
; offset someArray  8 
	PUSH EBP
	MOV  EBP, ESP
	MOV  EDI, [EBP+8]
	MOV  ECX, [EBP+12]
makeList:
	MOV  EAX, [EBP+20]
	SUB  EAX, [EBP+16]
	INC  EAX
	CALL RandomRange
	ADD  EAX, [EBP+16]
	MOV  [EDI], EAX
	ADD  EDI, 4
	LOOP makeList

	POP  EBP
	RET  16
fillArray ENDP
sortList PROC
; parameters: someArray (reference, input/output), ARRAYSIZE (value, input)
; ARRAYSIZE		 12
; offset someArray   8
	PUSH EBP
	MOV  EBP, ESP
	MOV  EDI, [EBP+8]
	MOV  ECX, [EBP+12]
	DEC  ECX
	MOV  EBX, 0
outerLoop:
	MOV  EDX, EBX
	MOV  EAX, EBX
	INC  EDX
	PUSH ECX
	MOV  ECX, [EBP+12]
	SUB  ECX, EBX
innerLoop:
	MOV  ESI, [EDI+(EDX*4)]
	CMP  ESI, [EDI+(EAX*4)]
	JLE  dontSwap
	MOV  EAX, EDX
dontSwap:
	INC  EDX
	LOOP innerLoop
	JMP  nextStep
nextStep:
	PUSH ESI
	PUSH EDX
	PUSH [EDI+(EBX*4)] ; someArray1
	PUSH [EDI+(EAX*4)] ; someArray2
	CALL exchangeElements
	POP  [EDI+(EAX*4)] ; someArray2
	POP  [EDI+(EBX*4)] ; someArray1
	POP  EDX 
	POP  ESI
	POP  ECX 
	INC  EBX
	LOOP outerLoop

	POP  EBP
	RET  8
sortList ENDP
exchangeElements PROC
; parameters: someArray[i] (reference. input/output), someArray[j] (reference, input/output), where i and j are the indexes of elements to be exchanged
	PUSH EBP
	MOV  EBP, ESP
	MOV  ESI, [EBP+8]
	MOV  EDX, [EBP+12]
	MOV  [EBP+12], EDX
	MOV  [EBP+8], ESI
	POP  EBP
	RET
exchangeElements ENDP
displayMedian PROC
; parameters: someTitle (reference, input), someArray (reference, input), ARRAYSIZE (value, input)
; ARRAYSIZE	     16
; offset someArray  12
; offset showMed	8
     PUSH EBP
	MOV  EBP, ESP
	MOV  EDI, [EBP+12]
	MOV  ECX, [EBP+16]

	MOV  ECX, EAX
	MOV  EBX, ARRAYSIZE
	CDQ
	DIV  EBX
	CMP  EDX, 0
	JE   evenNum
	CALL Crlf
	MOV  EDX, [EBP+8]
	CALL WriteString
	MOV  EAX, [EDI+(EAX+4)]
	CALL WriteDec
	CALL Crlf
	JMP theEnd
evenNum:
	MOV EBX, 4
	MUL EBX
	ADD EDI, EAX
	MOV EAX, [EDI]

	MOV EAX, EDI
	SUB EAX, 4
	MOV EDI, EAX
	MOV EAX, [EDI]

	ADD EAX, EDI
	MOV EDX, 0
	MOV EBX, 2
	CDQ
	DIV EBX

	CALL Crlf
	MOV EDX, [EBP+8]
	CALL WriteString
	CALL WriteDec
	CALL Crlf
	JMP theEnd

theEnd:
	POP  EBP
	RET
displayMedian ENDP
displayList PROC
; parameters: someTitle (reference, input), someArray (reference, input), ARRAYSIZE (value, input)
; offset spaces      20
; offset someArray   16
; offset showTitle   12
; ARRAYSIZE	      8
	PUSH EBP
	MOV  EBP, ESP

	MOV  EDI, [EBP+16]
	MOV  ECX, [EBP+8]
	MOV  ESI, 20

	CALL Crlf
	MOV  EDX, [EBP+12] ; show title
	CALL WriteString
	CALL Crlf

showElements:
	MOV  EAX, [EDI]
	CALL WriteDec
	MOV  EDX, [EBP+20]
	CALL WriteString
	ADD  EDI, 4

	DEC  ESI
	CMP  ESI, 0
	JG   sameLine
	CALL Crlf
	MOV  ESI, 20
	LOOP showElements
	JMP  theEnd
sameLine:
	LOOP showElements
theEnd:
	POP EBP
	RET 16
displayList ENDP
countList PROC
;	offset someArray ; 24
;	offset someArray ; 2o
;	ARRAYSIZE ; 16
;	LO ; 12
;	HI ; 8
	PUSH EBP
	MOV  EBP, ESP
	MOV  EDX, 1
	MOV  EDI, [EBP+20]
	MOV  ECX, [EBP+16]
	MOV  EBX, [EDI]

countLoop:
	SUB  EBX, [EBP+12]
	MOV  ESI, [EBP+24]
	ADD  ESI, EBX
	ADD  [ESI], EDX
	MOV  EAX, [ESI]
	CALL WriteDec
	ADD  EDI, 4
	MOV  EBX, [EDI]
	LOOP countLoop

	POP  EBP
	RET  20
countList ENDP
farewell PROC
	PUSH EBP
	MOV  EBP, ESP
	CALL Crlf
	CALL Crlf
	MOV  EDX, [EBP+8]
	CALL WriteString
	CALL Crlf
	POP  EBP
	RET  4
farewell ENDP

END main