package com.example.algorithm

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val stats = Array(n) {
        br.readLine().split(" ").map { it.toInt() }
    }

    var answer = Int.MAX_VALUE
    val visited = BooleanArray(n)
    visited[0] = true  // 첫 번째 사람은 항상 스타트팀에 포함
    
    fun teamDiff(): Int {
        var power1 = 0
        var power2 = 0
        for (i in 0 until n) {
            for (j in i+1 until n) {
                if (visited[i] && visited[j])
                    power1 += stats[i][j] + stats[j][i]
                else if (!visited[i] && !visited[j])
                    power2 += stats[i][j] + stats[j][i]
            }
        }
        return Math.abs(power1 - power2)
    }
    
    fun backTracking(count: Int, start: Int) {
        if (count == n / 2) {
            answer = minOf(answer, teamDiff())
            return
        }
        
        // 차이가 0이면 더 이상 탐색할 필요 없음
        if (answer == 0) return
        
        for (i in start until n) {
            if (!visited[i]) {
                visited[i] = true
                backTracking(count + 1, i + 1)  // i + 1로 수정
                visited[i] = false
            }
        }
    }
    
    backTracking(1, 1)
    println(answer)
}