import { ref } from 'vue'


export function useSudoku() {
    const board = ref()

	function createBoard() {
		return Array.from({ length: 9 }, () =>
			Array.from({ length: 9 }, () => ({
				value: 0,
				isSolved: false
			}))
		)
	}

	function loadEmpty() {
		board.value = createBoard()
	}

	function isValid(rowIndex: number, colIndex: number, candidate: number): boolean {
        // 檢查 row, column
        for (let i = 0; i < 9; i++) {
            // row 
            if (board.value[rowIndex][i].value === candidate) return false
            // column
            if (board.value[i][colIndex].value === candidate) return false
        }
        // 檢查 3x3 
        // 3x3 區塊起點
        const boxStartRow = Math.floor(rowIndex / 3) * 3
        const boxStartCol = Math.floor(colIndex / 3) * 3
        // 開始檢查 3x3
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (board.value[boxStartRow + i][boxStartCol + j].value === candidate) {
                    return false
                }
            }
        }
        return true
    }

    const backtracking = (): boolean => {
        // 找下一個空格
        for (let rowIndex = 0; rowIndex < 9; rowIndex++) {
            for (let colIndex = 0; colIndex < 9; colIndex++) {
                if (board.value[rowIndex][colIndex].value !== 0) continue
                // 嘗試 1~9
                for (let candidate = 1; candidate <= 9; candidate++) {
                    if (isValid(rowIndex, colIndex, candidate)) {
                        // 放入數字
                        board.value[rowIndex][colIndex].value = candidate
                        board.value[rowIndex][colIndex].isSolved = true
                        // 往下遞迴
                        if (backtracking()) return true
                        // 回溯
                        board.value[rowIndex][colIndex].value = 0
                        board.value[rowIndex][colIndex].isSolved = false
                    }
                }
                // 這格無解
                return false
            }
        }
        // 沒有空格 = 解完
        return true
    }

    function solve() {
        backtracking()
    }

    return {
        board,
        loadEmpty, solve
    }
}