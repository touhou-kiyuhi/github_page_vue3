<script setup lang="ts" name="SudokuSolver">
	import { onMounted } from 'vue'
    import { useSudoku } from '@/hooks/useSudokuSolver'

    const { board, loadEmpty, solve } = useSudoku()

	onMounted(() => {
		loadEmpty()
	})
</script>

<template>
    <div class="sudoku-container">
        <div class="sudoku-wrapper">
            <div class="sudoku-header">
                <h2>Sudoku</h2>
                <div class="sudoku-action-buttons">
                    <button class="sudoku-button" @click="loadEmpty">Reset</button>
                    <button class="sudoku-button" @click="solve">Solve</button>
                </div>
            </div>
            <div class="sudoku-grid">
                <div v-for="(row, i) in board" :key="i" class="sudoku-row">
                    <input
                        class="sudoku-cell" :class="cell.isSolved ? 'solved' : 'user'"
                        v-for="(cell, j) in row" :key="j"
                        v-model.number="cell.value"
                        maxlength="1"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .sudoku-container {
        width: 100%;
        max-width: 100%;
        padding: 8px;
        box-sizing: border-box;
    }

    .sudoku-wrapper {
        width: min(100%, 450px);
        margin: 0 auto;
    }

    /* Header */
    .sudoku-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 8px;
    }

    /* 按鈕區 */
    .sudoku-action-buttons {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }

    /* 響應式按鈕 */
    .sudoku-button {
        color: #333;
        border: 3px solid #333;
        background-color: white;
        cursor: pointer;

        font-size: clamp(12px, 2.5vw, 16px);
        padding: clamp(6px, 1.5vw, 12px) clamp(10px, 2vw, 16px);

        white-space: nowrap;
    }

    .sudoku-button:hover {
        background-color: #ddd;
    }

    .sudoku-grid {
        width: min(100%, 450px); /* 不超過父層 */
        aspect-ratio: 1 / 1;
        margin: 0 auto;

        border: 3px solid black;

        display: grid;
        grid-template-rows: repeat(9, 1fr);
    }

    /* 每列 */
    .sudoku-row {
        display: grid;
        grid-template-columns: repeat(9, 1fr);
    }

    /* 格子（關鍵修正） */
    .sudoku-cell {
        width: 100%;
        height: 100%;
        min-width: 0;   /* 防止 input 撐爆 */
        min-height: 0;  /* 防止撐高 */

        aspect-ratio: 1 / 1;
        text-align: center;

        font-size: clamp(12px, 4vw, 20px);

        border: 1px solid #ccc;
        box-sizing: border-box;

        padding: 0; /* 避免內距撐開 */
    }

    /* 3x3 粗線 */
    .sudoku-row:nth-child(3n) .sudoku-cell {
        border-bottom: 3px solid black;
    }
    .sudoku-cell:nth-child(3n) {
        border-right: 3px solid black;
    }
    /* 移除最外層重疊 */
    .sudoku-row:nth-child(9n) .sudoku-cell {
        border-bottom: 0;
    }
    .sudoku-cell:nth-child(9n) {
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
</style>