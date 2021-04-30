
const routes = [
  // { path: 'dashboard', component: () => import('pages/dashboard.vue') },
  {
    path: '/',
    component: () => import('layouts/iMaskerYA_Layout.vue'),
    children: [
      { path: 'dashboard', component: () => import('pages/dashboard.vue') },
      { path: 'history', component: () => import('pages/history.vue') },
      { path: 'about_us', component: () => import('pages/about_us.vue') },
      { path: '/',  redirect: '/dashboard' },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  // {
  //   path: '*',
  //   component: () => import('pages/dashboard.vue')
  // }
]

export default routes
