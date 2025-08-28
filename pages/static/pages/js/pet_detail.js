document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('popup');
  const openBtn = document.getElementById('openPopup');
  const closeBtn = document.querySelector('.close');

  openBtn.onclick = () => modal.style.display = 'flex';
  closeBtn.onclick = () => modal.style.display = 'none';
  window.onclick = (e) => {
    if (e.target === modal) modal.style.display = 'none';
  };
});
