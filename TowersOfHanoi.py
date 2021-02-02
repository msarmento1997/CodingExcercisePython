def tower(n, start, end, middle):
    if n == 1:
        print(f"Move {n} from tower {start} to tower {end}")
    else: 
        tower(n-1, start, middle, end)
        print(f"Move {n} from tower {start} to tower {end}")
        tower(n-1, middle, end, start)

tower(4, "A", "C", "B")