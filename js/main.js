/**
 * Pulso Fortal — Shared JavaScript
 * Navigation, data loading, chart rendering
 */

// Active nav link
(function() {
  const current = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === current || (current === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
})();

// Format currency (BRL)
function formatBRL(value) {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
}

// Format number
function formatNum(value) {
  return new Intl.NumberFormat('pt-BR').format(value);
}

// Format percentage
function formatPct(value) {
  return (value > 0 ? '+' : '') + value.toFixed(1) + '%';
}

// Load JSON data
async function loadData(path) {
  try {
    const resp = await fetch(path);
    return await resp.json();
  } catch (e) {
    console.error('Failed to load:', path, e);
    return null;
  }
}

// Simple bar chart renderer (no external deps)
function renderBarChart(containerId, data, options = {}) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const { labelKey = 'label', valueKey = 'value', color = 'var(--color-accent)', maxValue = null } = options;
  const max = maxValue || Math.max(...data.map(d => d[valueKey]));

  container.innerHTML = data.map(d => {
    const pct = (d[valueKey] / max) * 100;
    return `
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
        <div style="width:140px;font-size:0.9rem;text-align:right;color:var(--color-text-secondary);flex-shrink:0;font-weight:500;">${d[labelKey]}</div>
        <div style="flex:1;background:var(--color-surface-alt);border-radius:4px;height:28px;overflow:hidden;">
          <div style="height:100%;width:${pct}%;background:${color};border-radius:4px;transition:width 0.5s ease;display:flex;align-items:center;justify-content:flex-end;padding-right:8px;min-width:${d[valueKey] > 0 ? '40px' : '0'};">
            <span style="font-size:0.8rem;color:white;font-weight:600;">${d[valueKey]}</span>
          </div>
        </div>
      </div>`;
  }).join('');
}
