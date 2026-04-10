<script setup lang="ts" name="TheBattleCatsPortfolio">
    import BlogGallery from '@/components/blog/BlogGallery.vue'
</script>

<template>
    <main class="the-battle-cats-portfolio-main">
        <section class="introduction">
            <h1>Welcome to The Battle Cats Portfolio</h1>
        </section>
        <BlogGallery portfolio-path="/json/categories/game/theBattleCats/theBattleCatsPortfolio.json"/>
    </main>
</template>

<style scoped>
    .the-battle-cats-portfolio-main {
        flex: 1;
        padding: 20px;
    }

    .the-battle-cats-portfolio-main .introduction p {
        font-size: 18px;
    }
</style>