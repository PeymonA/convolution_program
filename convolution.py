def reader(data):
    in_arr = []
    in_file = data.readlines()

    for i in range(len(in_file)):
        temp_line = in_file[i].split(",")
        temp_line[-1] = temp_line[-1][:-1]
        for j in range(len(temp_line)):
            temp_line[j] = int(temp_line[j])
        in_arr.append(temp_line)

    return in_arr


def main():
    inputArray = open("data/data1.txt", "r")
    kernel = open("filters/filter1.txt", "r")
    in_arr = reader(inputArray)
    ker = reader(kernel)

    ker.reverse()
    for i in range(len(ker)):
        ker[i].reverse()

    convolution(in_arr, ker)

    inputArray.close()
    kernel.close()


def convolution(in_arr, ker):
    out_f = open("output.txt", "w")
    for i in range(len(in_arr)):
        for j in range(len(in_arr[i])):
            temp_list = []
            x = 0
            for n in range(i - 2, i + 3):
                y = 0
                for m in range(j - 2, j + 3):
                    if n < 0 or m < 0 or n > len(in_arr) - 1 or m > len(in_arr[j]) - 1:
                        temp_list.append(0)
                    else:
                        arr_val = in_arr[n][m]
                        ker_val = ker[x][y]
                        value = arr_val * ker_val
                        temp_list.append(value)
                    y += 1
                x += 1
            sum_val = sum(temp_list)
            final_val = sum_val // 16
            if final_val > 16:
                out_f.write("16 ")
            elif final_val < -16:
                out_f.write("-16 ")
            else:
                out_f.write(str(final_val) + " ")
        out_f.write("\n")
    out_f.close()


main()
