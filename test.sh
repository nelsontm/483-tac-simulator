tac() {
    for file in samples/*.tac; do
        prog=$(echo $file | cut -d'.' -f1 | cut -d'/' -f2)
        python3 tacsim.py $file > test/$prog.out 2>&1
    done
}

tac