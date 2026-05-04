<script setup lang="ts" name="TheBattleCatsPortfolio">
    import BlogGallery from '@/components/blog/BlogGallery.vue'
</script>

<template>
    <section class="introduction">
        <h1>Welcome to The Battle Cats Portfolio</h1>
    </section>
    <BlogGallery portfolio-path="/json/categories/game/theBattleCats/theBattleCatsPortfolio.json" />
</template>

<style scoped>
    .introduction p {
        font-size: 18px;
    }
</style>