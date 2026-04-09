import { createRouter, createWebHistory } from 'vue-router'

import WelcomePage from '@/pages/WelcomePage.vue'
import ProfileCard from '@/components/ProfileCard.vue'

import HomePage from '@/pages/HomePage.vue'
import Home from '@/pages/home/Home.vue'

import CategoriesPage from '@/pages/CategoriesPage.vue'
import Categories from '@/pages/categories/Categories.vue'

import AboutPage from '@/pages/AboutPage.vue'


const router = createRouter({
    // 專案名稱作為 Base URL
    history: createWebHistory('/github_page_vue3/'),
    routes: [
        {
            name: 'welcomePage', path: '/', component: WelcomePage, meta: { title: 'touhou-kiyuhi' }, 
            children: [
                { name: 'welcomeProfileCard', path: '', component: ProfileCard, }
            ]
        }, 
        {
            name: 'homePage', path: '/home',  component: HomePage, 
            children: [
                { name: 'Home', path: '', component: Home, meta: { title: 'touhou-kiyuhi - Home' } }
            ]
        },
        {
            name: 'CategoriesPage', path: '/categories', component: CategoriesPage, 
            children: [
                { name: 'Categories', path: '', component: Categories, meta: { title: 'touhou-kiyuhi - Categories' } }
            ]
        },
        {
            name: 'AboutPage', path: '/about', component: AboutPage, meta: { title: 'touhou-kiyuhi - About' }
        },
    ],
})

router.afterEach((to) => {
    // 從 matched routes 找第一個有 title 的 meta
    const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title)
    if (nearestWithTitle) {
        document.title = nearestWithTitle.meta.title as string
    } else {
        document.title = 'touhou-kiyuhi'
    }
})


export default router
