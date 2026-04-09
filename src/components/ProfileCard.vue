<script setup lang="ts" name="ProfileCard">
    import mika from '@/assets/mikaEatingRollCake.gif'
    import { computed } from 'vue'
    import { useRoute } from 'vue-router'
    import useMail from '@/hooks/useMail'


    const route = useRoute()
    const isWelcome = computed(() => route.path === '/')
    
    const socialLinks = [
        { id: "github", icon: "fa-brands fa-github", link: "https://github.com/touhou-kiyuhi" }, 
        { id: "twitter", icon: "fa-brands fa-twitter", link: "https://x.com/kiyuhi_touhou" }, 
        { id: "linkedin", icon: "fa-brands fa-linkedin", link: "https://www.linkedin.com/in/%E5%A7%AC%E9%9B%AA%E6%9F%8A-%E6%9D%B1%E6%96%B9-a41b69345/" }, 
        { id: "instagram", icon: "fa-brands fa-instagram", link: "https://www.instagram.com/kiyuhi_touhou/" }, 
        { id: "youtube", icon: "fa-brands fa-youtube", link: "https://www.youtube.com/@%E6%9D%B1%E6%96%B9%E5%A7%AC%E9%9B%AA%E6%9F%8A" }
    ]

    const { mailContact } = useMail()
</script>

<template>
    <div class="profile-card">
        <img :src="mika" alt="卯咪！！" title="窩是隻卯咪！！ 嗷嗷嗷！！">
        <h1>東方姫雪柊</h1>
        <p class="title">Computer Science Student 🐾</p>
        <p>{{ isWelcome ? '🐾 小雪 🐾' : 'National Taitung University' }}</p>
        <div class="social-links">
            <a 
                v-for="socialLink in socialLinks" :key="socialLink.id" 
                :href="socialLink.link" target="_blank"
            ><i :class="socialLink.icon"></i></a>
        </div>
        <!-- 歡迎頁面 -->
        <p v-if="isWelcome">
            <RouterLink to="/home" class="button-link">
                <button> Home </button>
            </RouterLink>
        </p>
        <!-- 不是歡迎頁面 -->
        <p v-else>
            <a href="#contact" @click="mailContact">
                <button><i class="fa-solid fa-envelope"></i> Contact </button>
            </a>
        </p>
    </div>
</template>

<style scoped>
    .profile-card {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        max-width: 300px;
        margin: auto;
        text-align: center;
        background-color: white;
    }

    .profile-card img {
        width: 100%;
    }

    .profile-card .title {
        color: black;
        font-size: 18px;
    }

    .profile-card button {
        border: none;
        outline: 0;
        display: inline-block;
        padding: 8px;
        color: white;
        background-color: black;
        text-align: center;
        cursor: pointer;
        width: 100%;
        font-size: 18px;
    }

    .profile-card a {
        text-decoration: none;
        font-size: 22px;
        color: black;
    }

    .profile-card button:hover, .profile-card a:hover {
        opacity: 0.7;
    }

    .social-links {
        display: flex;
        justify-content: center;
        gap: 5px;
    }
</style>