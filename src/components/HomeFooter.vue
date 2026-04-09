<script setup lang="ts" name="HomeFooter">
    import useMail from '@/hooks/useMail'


    const links = [
        { id: "home-link", name: "Home", path: "/home" }
    ]
    const { mailContact } = useMail()
    const socialLinks = [
        { id: "github", icon: "fa-brands fa-github", link: "https://github.com/touhou-kiyuhi" }, 
        { id: "twitter", icon: "fa-brands fa-twitter", link: "https://x.com/kiyuhi_touhou" }, 
        { id: "linkedin", icon: "fa-brands fa-linkedin", link: "https://www.linkedin.com/in/%E5%A7%AC%E9%9B%AA%E6%9F%8A-%E6%9D%B1%E6%96%B9-a41b69345/" }, 
        { id: "instagram", icon: "fa-brands fa-instagram", link: "https://www.instagram.com/kiyuhi_touhou/" }, 
        { id: "youtube", icon: "fa-brands fa-youtube", link: "https://www.youtube.com/@%E6%9D%B1%E6%96%B9%E5%A7%AC%E9%9B%AA%E6%9F%8A" }
    ]
</script>

<template>
    <footer>
        <p>&copy; 2026 Kiyuhi Touhou Website. All rights reserved.</p>
        <p>This site is built with love, code, and a bit of cat energy. 🐾</p>
        <div class="footer-links">
            <nav>
                <ul>
                    <li v-for="link in links" :key="link.id">
                        <RouterLink :to="link.path" :id="link.id"> {{ link.name }} </RouterLink>
                    </li>
                    <!-- 待設計 -->
                    <!-- <li><a href="#privacy">Privacy Policy</a></li> -->
                    <!-- <li><a href="#terms">Terms</a></li> -->
                    <li><a href="#contact" @click="mailContact">Contact</a></li>
                </ul>
            </nav>
        </div>
        <div class="social-links">
            <a 
                v-for="socialLink in socialLinks" :key="socialLink.id" 
                :href="socialLink.link" target="_blank"
            ><i :class="socialLink.icon"></i></a>
        </div>
    </footer>
</template>

<style scoped>
    footer {
        background-color: #333;
        color: white;
        padding: 10px 20px;
        text-align: center;
    }

    footer a {
        text-decoration: none;
    }

    .footer-links nav ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
    }

    .footer-links nav ul li {
        display: inline-block;
        margin: 0 10px;
    }

    .footer-links nav ul li a {
        color: white;
    }

    .social-links {
        display: flex;
        justify-content: center;
        margin-top: 10px;
        gap: 12px;
    }

    .social-links a {
        color: white;
        font-size: 24px;
        transition: color 0.3s;
    }

    .social-links a:hover {
        color: #ffcc00; /* 滑過時變色（可換） */
    }
</style>