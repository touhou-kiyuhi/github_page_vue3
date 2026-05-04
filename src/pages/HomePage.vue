<script setup lang="ts" name="HomePage">
    import HomeHeader from '@/components/HomeHeader.vue'
    import HomeFooter from '@/components/HomeFooter.vue'
    import HomeAside from '@/components/HomeAside.vue'

    import { useRoute } from 'vue-router'
    import { computed } from 'vue'


    const route = useRoute()
    const showAside = computed(() => route.meta.showAside !== false)
</script>

<template>
    <!-- Header -->
    <HomeHeader />
    <div class="content-wrapper">
        <!-- Aside -->
        <HomeAside v-if="showAside" />
        <!-- Main -->
        <RouterView />
    </div>
    <!-- Footer -->
    <HomeFooter />
</template>

<style scoped>
    
</style>