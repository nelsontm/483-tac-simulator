tac() {
    for file in samples/*.tac; do
        python3 tacsim.py $file > test/$file 2>&1
    done
}

tac