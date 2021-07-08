def question(n):
    if n < 10 and n > 0:
        n = "0" + str(n)
    print("\n\n","---" * 26, "\n\n Questão {} \n\n".format(n))
