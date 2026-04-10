<script setup lang="ts" name="Utilities">
    import { computed } from 'vue'
    import { useRoute } from 'vue-router'


    const route = useRoute()
    const utilitiesName = computed(() => {
        const title = route.meta.title as string | null
        return title?.split(' - ')[1] ?? 'Utilities'
    })
</script>

<template>
    <main class="utilities-main">
        <section class="introduction">
            <h1>Utilities - {{ utilitiesName }}</h1>
        </section>
        <div style="justify-items: center;">
            <RouterView />
        </div>
    </main>
</template>

<style scoped>
    .utilities-main {
        flex: 1;
        padding: 20px;
    }

    .utilities-main .introduction p {
        font-size: 18px;
    }
</style>