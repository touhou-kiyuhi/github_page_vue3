<script setup lang="ts" name="CategoriesPage">
    import HomeHeader from '@/components/HomeHeader.vue'
    import HomeFooter from '@/components/HomeFooter.vue'
    import HomeAside from '@/components/HomeAside.vue'
</script>

<template>
    <!-- Header -->
    <HomeHeader/>
    <div class="content-wrapper">
        <!-- Aside -->
        <HomeAside/>
        <!-- Main -->
        <RouterView/>
    </div>
    <!-- Footer -->
    <HomeFooter/>
</template>

<style scoped>
    
</style>