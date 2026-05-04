<script setup lang="ts" name="WelcomePage">
    import ProfileCard from '@/components/ProfileCard.vue'
</script>

<template>
    <div class="content-wrapper">
        <main class="welcome-main">
            <div class="profile-card-wrapper">
                <ProfileCard />
            </div>
        </main>
    </div>
</template>

<style scoped>
    .welcome-main {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    .profile-card-wrapper {
        max-width: 400px;
        width: 100%;
    }
</style>