import Foundation
class Solution {
    func reverse(_ x: Int) -> Int {
        var sign = 1
        if x < 0 {
            sign = -1
        }

        var tmp = x;
        var result = 0

        while tmp != 0 {
            result = result * 10 + tmp % 10
            tmp /= 10
        }

        let maxInt = Int(Int32.max)
        let minInt = Int(Int32.min)

        if result > maxInt || result < minInt {
            return 0
        }
        return result
    }
}
