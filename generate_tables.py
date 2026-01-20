for i in range(2,21):
    filename = f"tables/table_{i}.txt";
    with open(filename,"w") as f:
        f.write(f"Multiplication Table of {i}\n");
        f.write("----------------------------\n");

        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n");
