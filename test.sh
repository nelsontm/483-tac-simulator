tac() {
    for file in samples/*.tac; do
        prog=$(echo $file | cut -d'.' -f1 | cut -d'/' -f2)
        python3 tacsim.py $file > test/$prog.tac 2>&1
    done
}

mkdir test
tac