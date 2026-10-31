/* FreePhoto official contact control. Does not transmit any photo data. */
(() => {
  'use strict';
  const button = document.getElementById('fp-copy-wechat');
  const status = document.getElementById('fp-copy-status');
  if (!button || !status) return;
  const wechatId = button.getAttribute('data-wechat-id') || '';
  if (!/^[A-Za-z][A-Za-z0-9_-]{5,19}$/.test(wechatId)) {
    button.disabled = true;
    status.textContent = '微信号暂不可用，请从个人官网联系。';
    return;
  }
  async function copyText(value) {
    if (navigator.clipboard && window.isSecureContext) {
      try {
        await navigator.clipboard.writeText(value);
        return true;
      } catch (_) { /* Try legacy fallback. */ }
    }
    const temporary = document.createElement('textarea');
    temporary.value = value;
    temporary.setAttribute('readonly', '');
    temporary.setAttribute('aria-hidden', 'true');
    temporary.style.position = 'fixed';
    temporary.style.top = '-9999px';
    document.body.appendChild(temporary);
    temporary.focus();
    temporary.select();
    let copied = false;
    try { copied = document.execCommand('copy'); } catch (_) { copied = false; }
    temporary.remove();
    button.focus();
    return copied;
  }
  button.addEventListener('click', async () => {
    button.disabled = true;
    try {
      const copied = await copyText(wechatId);
      status.textContent = copied
        ? '已复制微信号 ' + wechatId + '，打开微信搜索添加即可。'
        : '复制失败，请长按选择微信号 ' + wechatId + ' 进行复制。';
      if (copied) button.textContent = '复制成功 ✓';
    } catch (_) {
      status.textContent = '复制失败，请手动复制微信号 ' + wechatId + '。';
    } finally {
      button.disabled = false;
    }
  });
})();
