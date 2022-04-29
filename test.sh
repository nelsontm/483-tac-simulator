tac() {
    for file in samples/*.tac; do
        prog=$(echo $file | cut -d'.' -f1 | cut -d'/' -f2)
        if [ "$(ls samples/$prog.in 2>/dev/null | wc -l)" == 1 ]
            then
            python3 tacsim.py $file < samples/$prog.in > test/$prog.out 2>&1
            else
            python3 tacsim.py $file > test/$prog.out 2>&1
        fi
    done
}

tac