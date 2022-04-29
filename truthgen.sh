SPIM=/afs/umich.edu/user/c/h/chhsiao/Public/spim

asm() {
    for file in samples/*.decaf; do
        prog=$(echo $file | cut -d'.' -f1 | cut -d'/' -f2)
        dcc/dcc < $(echo $file) > samples/$prog.asm 2>&1
        echo "compiling $prog"
    done
}

tac() {
    for file in samples/*.decaf; do
        prog=$(echo $file | cut -d'.' -f1 | cut -d'/' -f2)
        dcc/dcc -d tac < $(echo $file) > samples/$prog.tac 2>&1
        echo "compiling $prog"
    done
}

out() {
    for file in samples/*.decaf; do
        prog=$(echo $file | cut -d'.' -f1 | cut -d'/' -f2)
        $SPIM -keepstats -file samples/$prog.asm > samples/$prog.stats
        echo "compiling $prog"
    done
}

tac