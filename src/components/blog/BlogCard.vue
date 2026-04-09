<script setup lang="ts" name="BlogCard">
    import type { IF_PostSrc } from '@/types/post'
    import catInBox from '@/assets/logo.svg'


    const props = defineProps<{ 
        post: IF_PostSrc 
    }>()
</script>

<template>
    <RouterLink :to="{
        name: 'VideoPost', 
        params: { tags: props.post.tags.join('/') },
        query: { id: props.post.id }
    }" class="blogcard-link">
        <article>
            <!-- 左側 Logo -->
            <div class="logo">
                <img :src="catInBox" alt="Site Logo" title="窩是隻卯咪！！ 嗷嗷嗷！！">
            </div>
            <!-- 右側內容 -->
            <div class="card-content">
                <h3>🐾{{ props.post.name }}🐾</h3>
            </div>
        </article>
    </RouterLink>
</template>

<style scoped>
    .blogcard-link {
        text-decoration: none;
        color: inherit;
        display: block;
    }
    article {
        display: flex;
        align-items: center; /* 讓 logo 和內容垂直置中 */
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin: 20px;
        cursor: pointer;
        transition: transform 0.3s ease-in-out;
        max-width: 100%;
        overflow: hidden; /* 防止內容溢出 */
        width: 350px; /* 固定寬度 */
    }

    article:hover {
        transform: scale(1.05);
    }
    
    article:active {
        transform: scale(0.98);
    }

    /* 左側 Logo 區塊 */
    .logo {
        width: 70px; /* 調整為更適合的大小 */
        height: 70px;
        display: flex;
        justify-content: center;
        align-items: center;
        border-top-left-radius: 10px;
        border-bottom-left-radius: 10px;
        overflow: hidden; /* 保證圖片不會超出範圍 */
        padding: 10px; /* 為 logo 加入內邊距 */
    }

    .logo img {
        width: 100%; /* 圖片自動填滿容器寬度 */
        height: 100%; /* 圖片高度設為 100% 以填滿區域 */
        object-fit: contain; /* 保持比例顯示圖片，不會拉伸 */
    }

    /* 右側內容區塊 */
    .card-content {
        padding: 15px;
        flex-grow: 1;
        background-color: #ffffff;
        margin-left: 5px; /* 讓內容區塊與 logo 區塊有間距 */
    }

    .card h3 {
        margin: 0;
        font-size: 1.4em;
        color: #333;
    }

    .card p {
        color: #555;
        font-size: 1em;
        margin-top: 10px;
    }
</style>