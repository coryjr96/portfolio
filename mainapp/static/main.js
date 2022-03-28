const mobileButton = document.getElementById('mobilecta')
                nav = document.querySelector('nav')
                mobileButtonExit = document.getElementById('mobileexit');
            mobileButton.addEventListener('click', () => {
                nav.classList.add('menu-btn');
            })
            mobileButtonExit.addEventListener('click', () => {
                nav.classList.remove('menu-btn');
            })