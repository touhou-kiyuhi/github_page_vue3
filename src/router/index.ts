import { createRouter, createWebHistory } from 'vue-router'

import WelcomePage from '@/pages/WelcomePage.vue'
import ProfileCard from '@/components/ProfileCard.vue'

import HomePage from '@/pages/HomePage.vue'
import Home from '@/pages/home/Home.vue'
import Categories from '@/pages/home/Categories.vue'

import AboutPage from '@/pages/AboutPage.vue'


const router = createRouter({
    // 專案名稱作為 Base URL
    history: createWebHistory('/github_page_vue3/'),
    routes: [
        {
            name: 'welcomePage', 
            path: '/',  
            component: WelcomePage, 
            children: [
                { name: 'welcomeProfileCard', path: '', component: ProfileCard }
            ]
        }, 
        {
            name: 'homePage', 
            path: '/home',  
            component: HomePage,
            children: [
                { name: 'Home', path: '', component: Home }, 
                { name: 'Categories', path: '/categories', component: Categories }, 
            ]
        },
        {
            name: 'AboutPage', 
            path: '/about', 
            component: AboutPage
        },
    ],
})


export default router
