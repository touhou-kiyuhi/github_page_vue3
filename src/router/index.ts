import { createRouter, createWebHistory } from 'vue-router'

import WelcomePage from '@/pages/WelcomePage.vue'
import ProfileCard from '@/components/ProfileCard.vue'

import HomePage from '@/pages/HomePage.vue'
import Home from '@/pages/home/Home.vue'

import CategoriesPage from '@/pages/CategoriesPage.vue'
import Categories from '@/pages/categories/Categories.vue'
import TheBattleCatsPortfolio from '@/pages/categories/TheBattleCatsPortfolio.vue'
import VideoPost from '@/pages/categories/VideoPost.vue'

import UtilitiesPage from '@/pages/UtilitiesPage.vue'
import Utilities from '@/pages/utilities/Utilities.vue'
import SudokuSolver from '@/pages/utilities/SudokuSolver.vue'

import AboutPage from '@/pages/AboutPage.vue'

import DemoPage from '@/pages/DemoPage.vue'
import Demo from '@/pages/demo/Demo.vue'


const router = createRouter({
    // 專案名稱作為 Base URL
    history: createWebHistory('/github_page_vue3/'),
    routes: [
        {
            name: 'welcomePage', path: '/', component: WelcomePage, 
            children: [
                { 
                    name: 'welcomeProfileCard', path: '', component: ProfileCard, 
                    meta: { title: 'touhou-kiyuhi' } 
                }
            ]
        }, 
        {
            name: 'homePage', path: '/home',  component: HomePage, 
            children: [
                { 
                    name: 'Home', path: '', component: Home, 
                    meta: { title: 'touhou-kiyuhi - Home' } 
                }
            ]
        },
        {
            name: 'AboutPage', path: '/about', component: AboutPage, 
            meta: { title: 'touhou-kiyuhi - About' }
        },
        {
            name: 'CategoriesPage', path: '/categories', component: CategoriesPage, 
            children: [
                { 
                    name: 'Categories', path: '', component: Categories, 
                    meta: { title: 'touhou-kiyuhi - Categories' } 
                }, 
                { 
                    name: 'The Battle Cats Portfolio', path: 'theBattleCatsPortfolio', component: TheBattleCatsPortfolio, 
                    meta: { title: 'touhou-kiyuhi - The Battle Cats Portfolio' } 
                }, 
                { 
                    name: 'VideoPost', path: 'videoPost/:tags', component: VideoPost, 
                    meta: { title: 'touhou-kiyuhi - VideoPost' } 
                }
            ]
        },
        {
            name: 'UtilitiesPage', path: '/utilities',  component: UtilitiesPage, 
            children: [
                { 
                    name: 'Utilities', path: '', component: Utilities, 
                    meta: { title: 'touhou-kiyuhi - Utilities' }, 
                    children: [
                        { 
                            name: 'Sudoku Solver', path: 'sudokuSolver', component: SudokuSolver, 
                            meta: { title: 'touhou-kiyuhi - Sudoku Solver' } 
                        }
                    ]
                    
                }
            ]
        },
        {
            name: 'DemoPage', path: '/demo', component: DemoPage, 
            children: [
                { 
                    name: 'Demo', path: '', component: Demo, 
                    meta: { title: 'touhou-kiyuhi - Demo' } 
                }
            ]
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
