<script setup lang="ts" name="VideoPost">
    import { ref, onMounted } from 'vue'
    import { useRoute } from 'vue-router'
    import { fetchJSON } from '@/hooks/useFetch'
    import type { IF_VideoPost } from '@/types/post'
    

    let route = useRoute()
    const videoPostData = ref<IF_VideoPost | null>(null)

    onMounted(async () => {
        try {
            const tags = route.params.tags as string
            const id = route.query.id as string
            videoPostData.value = await fetchJSON(`/json/categories/${tags}/${id}.json`)
        } catch (err) {
            console.error('Fetch demo.json failed:', err)
        }
    })
</script>

<template>
    <section class="introduction" v-if="videoPostData">
        <h1>{{ videoPostData?.title }}</h1>
        <p>{{ videoPostData?.description }}</p>
    </section>
    <section v-if="videoPostData?.videos.length" v-for="video in videoPostData?.videos" :key="video.id">
        <h2>{{ video.label }}</h2>
        <div class="video-container">
            <iframe :src="`https://www.youtube.com/embed/${video.id}`" 
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
            ></iframe>
        </div>
    </section>
</template>

<style scoped>
    .introduction p {
        font-size: 18px;
    }
    .video-container {
        display: flex;
        justify-content: center;
        margin: 1rem 0;
    }

    .video-container iframe {
        aspect-ratio: 16 / 9;
        width: 100%;
        max-width: 800px;
        border: none;
    }
</style>