// export type PostType = 'video' | 'others'

export interface IF_PostSrc {
	id: string
	name: string
	tags: string[]
}

// Video Type Post 
export interface IF_Video {
	id: string
	label: string
}
export interface IF_VideoPost {
	title: string
	description: string
	videos: IF_Video[]
}




// export type PostType = 'video' | 'grammar'

// export interface BasePost {
// 	id: string
// 	type: PostType
// 	title: string
// 	description: string
// 	category: string[]
// 	tags: string[]
// 	year: number
// }

// // 影片型文章
// export interface VideoPost extends BasePost {
// 	type: 'video'
// 	videos: {
// 		label: string
// 		youtubeId: string
// 	}[]
// }

// // 文法/教學型文章
// export interface GrammarPost extends BasePost {
// 	type: 'grammar'
// 	content: {
// 		themesData: {
// 			theme: string
// 			usage: string
// 			meaning: string
// 			notice: string
// 			sentence: {
// 				japanese: string
// 				chinese: string
// 			}[]
// 		}[]
// 		compareThemes: {
// 			title: string
// 			themes: string[]
// 		}
// 	}
// 	video?: {
// 		label: string
// 		youtubeId: string
// 	}
// }

// export type Post = VideoPost | GrammarPost

// // 精簡版 index.json
// export interface PostMeta {
// 	id: string
// 	type: PostType
// 	title: string
// 	category: string[]
// 	tags: string[]
// 	year: number
// }

// export interface IndexData {
// 	tags: string[]
// 	years: number[]
// 	posts: PostMeta[]
// }