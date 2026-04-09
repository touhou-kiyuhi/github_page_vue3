<script setup lang="ts" name="BlogGallery">
    import BlogCard from '@/components/blog/BlogCard.vue'
    import { computed, ref } from 'vue'
    
    // 處理 Filter
    const selectedTag = ref('all')
    const tagList = [
        { id: "all", name: "Show all" },
        { id: "test1", name: "Test 1" },
        { id: "test2", name: "Test 2" },
        { id: "test3", name: "Test 3" },
    ]
    const activeTag = computed(() => selectedTag.value)
    function selectTag(tagId: string) {
        selectedTag.value = tagId
    }
    // 模擬 data
    const dataList = [
        { id: "data1", name: "data 1", tag: "test1" },
        { id: "data2-1", name: "data 2-1", tag: "test2" },
        { id: "data2-2", name: "data 2-2", tag: "test2" },
        { id: "data2-3", name: "data 2-3", tag: "test2" },
        { id: "data3", name: "data 3", tag: "test3" },
        { id: "data4", name: "data 4", tag: "test4" },
        { id: "data5", name: "data 5", tag: "test5" },
        { id: "data6", name: "data 6", tag: "test6" },
        { id: "data7", name: "data 7", tag: "test7" },
        { id: "data8", name: "data 8", tag: "test8" },
        { id: "data9", name: "data 9", tag: "test9" },
        { id: "data10", name: "data 10", tag: "test10" },
    ]
    const filteredDataList = computed(() => {
        if (selectedTag.value === 'all') return dataList
        return dataList.filter(item => item.tag === selectedTag.value)
    })
</script>

<template>
    <div>
		<h2>PORTFOLIO</h2>
        <div id="filterButtonContainer">
            <button 
                v-for="tag in tagList" :key="tag.id" 
                class="btn" :class=" { active: activeTag === tag.id }"
                @click="selectTag(tag.id)"
            > {{ tag.name }} </button>
        </div>
        <div class="row">
            <div v-for="data in filteredDataList" :key="data.id" class="column">
                {{ data.name }}
                <!-- BlogCard -->
                <BlogCard :data="data"/>
            </div>
        </div>
	</div>
</template>

<style scoped>
    h2 {
        font-size: 50px;
        text-align: left;
        word-break: break-all;
        margin-bottom: 20px;  /* 給標題下方留點空間 */
    }

    #filterButtonContainer {
        flex-wrap: nowrap;      /* 不讓按鈕換行 */
        justify-content: flex-start;  /* 按鈕靠左排列 */
        margin-bottom: 20px;
        overflow-x: auto;      /* 如果按鈕超出範圍，則水平滾動 */
        gap: 10px; /* 按鈕之間的間距 */
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

    /* Grid container */
    .row {
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        justify-content: flex-start;  /* 卡片靠左排列 */
        margin: 0 -8px;
        max-width: 100%;
        padding: 0 8px;
    }

    /* Individual column style */
    .column {
        width: calc(20% - 16px);  /* 每行顯示 5 張卡片 */
        display: block;
        flex-shrink: 0;
        box-sizing: border-box;
    }

    .column img {
        width: 100%;
        height: auto;
        border-radius: 8px;
    }
    
    @media (max-width: 2050px) {
        .column {
            width: calc(25% - 16px);  /* 每行顯示 4 張卡片 */
        }
    }

    @media (max-width: 1700px) {
        .column {
            width: calc(33.33% - 16px);  /* 每行顯示 3 張卡片 */
        }
    }

    @media (max-width: 1500px) {
        .column {
            width: calc(50% - 16px);  /* 每行顯示 2 張卡片 */
        }
    }

    @media (max-width: 1100px) {
        .column {
            width: 100%;  /* 每行顯示 1 張卡片 */
        }
    }
</style>