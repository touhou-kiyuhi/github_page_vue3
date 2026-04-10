<script setup lang="ts" name="ProfileCard">
	import { ref, onMounted } from 'vue'


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

    function solve() {
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
        backtracking()
    }

	onMounted(() => {
		loadEmpty()
	})
</script>

<template>
    <h2>Sudoku</h2>
	<div class="grid">
		<div v-for="(row, i) in board" :key="i" class="row">
			<input
				v-for="(cell, j) in row"
				:key="j"
				v-model.number="cell.value"
				maxlength="1"
				class="cell"
				:class="cell.isSolved ? 'solved' : 'user'"
			/>
		</div>
	</div>
    <button class="btn" @click="loadEmpty">Reset</button>
	<button class="btn" @click="solve">Solve</button>
</template>

<style scoped>
    .grid {
        display: inline-block;
        border: 3px solid black;
    }

    .row {
        display: flex;
    }

    /* 基本格子 */
    .cell {
        width: 50px;
        height: 50px;
        text-align: center;
        font-size: 20px;
        border: 1px solid #ccc;
        color: black;
        box-sizing: border-box;
    }

    /* 3x3 粗線 */
    .row:nth-child(3n) .cell {
        border-bottom: 3px solid black;
    }
    .cell:nth-child(3n) {
        border-right: 3px solid black;
    }
    /* 移除最外層重疊 */
    .row:nth-child(9n) .cell {
        border-bottom: 0;
    }
    .cell:nth-child(9n) {
        border-right: 0;
    }

    /* 顏色 */
    .solved {
        color: red;
        font-weight: bold;
    }

    .user {
        color: black;
    }

    .btn {
        color: #333333;  /* 文字顏色設置為深色 */
        border: solid #333333;  /* 初始邊框顏色 */
        outline: none;
        padding: 12px 16px;
        margin: 5px;
        background-color: white;
        cursor: pointer;
        font-size: 16px;
        white-space: nowrap;  /* 防止按鈕文字換行 */
    }

    .btn:hover {
        background-color: #ddd;
    }

    .btn.active {
        background-color: #666;
        color: white;
    }
</style>