<script setup lang="ts" name="BlogGallery">
    import { ref, onMounted, computed } from 'vue'
    import type { IF_Portfolio, IF_Tag, IF_Post } from '@/types/post'
    import { fetchJSON } from '@/hooks/useFetch'
    import BlogCard from '@/components/blog/BlogCard.vue'
    
    
    const props = defineProps<{ 
        portfolioPath: string
    }>()

    const portfolioData = ref<IF_Portfolio>()
    const selectedTag = ref('all')
    const tagList = ref<IF_Tag[]>([
        { id: "all", name: "Show all" }
    ])
    const postList = ref<IF_Post[]>([])
    
    onMounted(async () => {
        try {
            if (!props.portfolioPath) return
            portfolioData.value = await fetchJSON(props.portfolioPath)
            if (!portfolioData.value) return
            tagList.value.push(...portfolioData.value.tagList)
            postList.value = portfolioData.value.postList
            console.log(postList)
        } catch (err) {
            console.error('Fetch demo.json failed:', err)
        }
    })
    // 處理 Filter
    const activeTag = computed(() => selectedTag.value)
    function selectTag(tagId: string) {
        selectedTag.value = tagId
    }
    const filteredPostList = computed(() => {
        const posts = postList.value ?? []
        if (selectedTag.value === 'all') return posts
        return posts.filter(item => item.tags.includes(selectedTag.value))
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
            <div v-for="post in filteredPostList" :key="post.id" class="column">
                {{ post.name }}
                <!-- BlogCard -->
                <BlogCard :post="post" />
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