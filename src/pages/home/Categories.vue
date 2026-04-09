<script setup lang="ts" name="Categories">
    import BlogGallery from '@/components/blog/BlogGallery.vue'
</script>

<template>
    <main class="categories-main">
        <section class="introduction">
            <h1>Welcome to Categories</h1>
        </section>
        <BlogGallery/>
    </main>
</template>

<style scoped>
    .categories-main {
        flex: 1;
        padding: 20px;
    }

    .categories-main .introduction p {
        font-size: 18px;
    }
</style>