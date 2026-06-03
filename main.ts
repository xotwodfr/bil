basic.forever(function () {
    if (bitbot.readLine(BBLineSensor.Left) == 0 && bitbot.readLine(BBLineSensor.Right) == 0) {
        bitbot.go(BBDirection.Forward, 50)
    } else if (bitbot.readLine(BBLineSensor.Left) == 1 && bitbot.readLine(BBLineSensor.Right) == 0) {
        bitbot.rotate(BBRobotDirection.Left, 50)
    } else if (bitbot.readLine(BBLineSensor.Left) == 0 && bitbot.readLine(BBLineSensor.Right) == 1) {
        bitbot.rotate(BBRobotDirection.Right, 50)
    } else {
        bitbot.go(BBDirection.Forward, 0)
    }
})
