<script setup lang="ts" name="Utilities">
    
</script>

<template>
    <main class="utilities-main">
        <section class="introduction">
            <h1>Utilities</h1>
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