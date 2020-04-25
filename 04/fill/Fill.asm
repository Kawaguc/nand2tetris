// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

//スクリーンを塗る動作は終了判定、塗る、インクリメントの動作をピクセル数回繰り返す
(LOOP)
    @i
    M=0

    @KBD
    D=M

    @BLACK
    D;JGT

    (WHITE)
        //終了判定
        @i
        D=M
        @8191
        D=D-A
        @LOOP
        D;JGT

        //塗る
        @i
        D=M
        @SCREEN
        A=A+D
        M=0
        
        // インクリメント
        @i
        M=M+1
    @WHITE
    0;JMP


    (BLACK)
        @i
        D=M
        @8191
        D=D-A
        @LOOP
        D;JGT

        @i
        D=M
        @SCREEN
        A=A+D
        M=-1

        @i
        M=M+1
    @BLACK
    0;JMP
