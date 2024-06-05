# n discs from src to dest using extra as temp space
def moveAllDiscs(n, src, extra, dest):
    if n == 1:
        print("Move 1st disc from", src, "to", dest)
        return
        # Moving all (n - 1) discs from src to extra
    # using dest as extraSpace
    moveAllDiscs(n - 1, src, dest, extra)
    print("Move", n, "th disc from", src, "to", dest)
    moveAllDiscs(n - 1, extra, src, dest)


moveAllDiscs(4, "source", "extraSpace", "destination")
