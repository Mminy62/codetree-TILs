if let input = readLine() {
    let startIndex = input.index(input.startIndex, offsetBy: 2)
    let endIndex = input.index(input.startIndex, offsetBy :9)
    print(input[startIndex...endIndex])
}