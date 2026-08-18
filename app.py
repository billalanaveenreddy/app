import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CareWatch — Elder Health Monitor",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .block-container { padding: 0 !important; }
    header { display: none !important; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@2.47.0/tabler-icons.min.css"/>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f5f4f0;color:#1a1a18}
.app{display:grid;grid-template-columns:240px 1fr;min-height:100vh}
.sidebar{background:#ebebE6;border-right:0.5px solid #d3d1c7;padding:16px 0;display:flex;flex-direction:column;gap:4px;position:fixed;top:0;left:0;height:100vh;width:240px;overflow-y:auto}
.sidebar-header{padding:12px 16px 16px;border-bottom:0.5px solid #d3d1c7;margin-bottom:8px}
.app-logo{font-size:15px;font-weight:500;color:#1a1a18;display:flex;align-items:center;gap:8px}
.app-logo .dot{width:8px;height:8px;border-radius:50%;background:#1D9E75}
.app-subtitle{font-size:11px;color:#888780;margin-top:2px}
.nav-item{display:flex;align-items:center;gap:10px;padding:8px 16px;font-size:13px;color:#5f5e5a;cursor:pointer;transition:background 0.15s;border-left:2px solid transparent}
.nav-item:hover{background:#f5f4f0;color:#1a1a18}
.nav-item.active{background:#ffffff;color:#1a1a18;font-weight:500;border-left:2px solid #1D9E75}
.nav-item i{font-size:16px;opacity:0.7}
.nav-item.active i{opacity:1}
.nav-section{font-size:10px;letter-spacing:0.08em;color:#888780;padding:12px 16px 4px;text-transform:uppercase}
.patient-mini{display:flex;align-items:center;gap:8px;padding:6px 16px;cursor:pointer;transition:background 0.15s}
.patient-mini:hover{background:#f5f4f0}
.patient-mini.selected{background:#ffffff}
.avatar{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:500;flex-shrink:0}
.avatar.green{background:#E1F5EE;color:#085041}
.avatar.blue{background:#E6F1FB;color:#0C447C}
.avatar.amber{background:#FAEEDA;color:#633806}
.avatar.coral{background:#FAECE7;color:#712B13}
.avatar.purple{background:#EEEDFE;color:#3C3489}
.mini-name{font-size:12px;color:#1a1a18;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mini-status{width:6px;height:6px;border-radius:50%;margin-left:auto;flex-shrink:0}
.status-ok{background:#1D9E75}
.status-warn{background:#EF9F27}
.status-alert{background:#E24B4A}
.main{margin-left:240px;display:flex;flex-direction:column;min-height:100vh}
.topbar{display:flex;align-items:center;justify-content:space-between;padding:12px 20px;border-bottom:0.5px solid #d3d1c7;background:#ffffff;position:sticky;top:0;z-index:10}
.topbar-left{display:flex;align-items:center;gap:12px}
.page-title{font-size:15px;font-weight:500;color:#1a1a18}
.date-badge{font-size:11px;color:#888780;padding:3px 8px;background:#f5f4f0;border:0.5px solid #d3d1c7;border-radius:8px}
.topbar-right{display:flex;align-items:center;gap:8px}
.icon-btn{width:32px;height:32px;border-radius:8px;border:0.5px solid #d3d1c7;background:#ffffff;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#5f5e5a;font-size:15px}
.icon-btn:hover{background:#f5f4f0}
.content{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:16px}
.summary-row{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.stat-card{background:#f5f4f0;border-radius:8px;padding:12px 14px;border:0.5px solid #d3d1c7}
.stat-label{font-size:11px;color:#888780;margin-bottom:6px;display:flex;align-items:center;gap:6px}
.stat-label i{font-size:14px}
.stat-value{font-size:22px;font-weight:500;color:#1a1a18;line-height:1}
.stat-sub{font-size:11px;color:#888780;margin-top:4px}
.stat-card.good .stat-value{color:#0F6E56}
.stat-card.warn .stat-value{color:#854F0B}
.stat-card.alert .stat-value{color:#A32D2D}
.section-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.section-title{font-size:13px;font-weight:500;color:#1a1a18}
.section-link{font-size:11px;color:#185FA5;cursor:pointer}
.patients-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.patient-card{background:#ffffff;border:0.5px solid #d3d1c7;border-radius:12px;padding:14px;cursor:pointer;transition:border-color 0.15s}
.patient-card:hover{border-color:#b4b2a9}
.patient-card.selected{border-color:#1D9E75;border-width:1.5px}
.pc-header{display:flex;align-items:flex-start;gap:10px;margin-bottom:10px}
.pc-avatar{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:500;flex-shrink:0}
.pc-info{flex:1;min-width:0}
.pc-name{font-size:13px;font-weight:500;color:#1a1a18}
.pc-meta{font-size:11px;color:#888780}
.pc-status-badge{font-size:10px;padding:2px 7px;border-radius:20px;font-weight:500;white-space:nowrap}
.badge-ok{background:#E1F5EE;color:#085041}
.badge-warn{background:#FAEEDA;color:#633806}
.badge-alert{background:#FCEBEB;color:#791F1F}
.vitals-row{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.vital-item{text-align:center;padding:6px;background:#f5f4f0;border-radius:6px}
.vital-icon{font-size:14px;color:#888780;margin-bottom:2px}
.vital-val{font-size:12px;font-weight:500;color:#1a1a18;line-height:1.2}
.vital-lbl{font-size:10px;color:#888780}
.two-col{display:grid;grid-template-columns:1fr 320px;gap:14px;align-items:start}
.side-panel{display:flex;flex-direction:column;gap:10px}
.detail-card{background:#ffffff;border:0.5px solid #d3d1c7;border-radius:12px;padding:14px}
.detail-header{display:flex;align-items:center;gap:10px;margin-bottom:12px;padding-bottom:10px;border-bottom:0.5px solid #d3d1c7}
.detail-avatar{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:500}
.detail-name{font-size:14px;font-weight:500;color:#1a1a18}
.detail-meta{font-size:11px;color:#888780}
.vitals-detail{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.vd-item{padding:8px 10px;background:#f5f4f0;border-radius:8px}
.vd-top{display:flex;align-items:center;gap:6px;margin-bottom:3px}
.vd-icon{font-size:15px}
.vd-label{font-size:11px;color:#888780}
.vd-value{font-size:14px;font-weight:500;color:#1a1a18}
.vd-range{font-size:10px;color:#888780;margin-top:1px}
.vd-normal .vd-icon{color:#1D9E75}
.vd-warn .vd-icon{color:#BA7517}
.vd-alert .vd-icon{color:#A32D2D}
.vd-alert .vd-value{color:#A32D2D}
.vd-warn .vd-value{color:#854F0B}
.log-btn{width:100%;margin-top:10px;padding:8px;border-radius:8px;border:0.5px solid #1D9E75;background:#E1F5EE;color:#085041;font-size:12px;cursor:pointer;font-weight:500;transition:background 0.15s}
.log-btn:hover{background:#9FE1CB}
.activity-list{display:flex;flex-direction:column}
.activity-item{display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:0.5px solid #ebebE6}
.activity-item:last-child{border-bottom:none}
.act-dot{width:7px;height:7px;border-radius:50%;margin-top:5px;flex-shrink:0}
.act-text{font-size:12px;color:#1a1a18;line-height:1.4}
.act-time{font-size:10px;color:#888780;margin-top:1px}
.add-btn{display:flex;align-items:center;gap:6px;font-size:12px;padding:5px 10px;border-radius:8px;border:0.5px solid #d3d1c7;background:#ffffff;color:#5f5e5a;cursor:pointer;transition:background 0.15s}
.add-btn:hover{background:#f5f4f0}
.modal-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.4);z-index:100;align-items:center;justify-content:center}
.modal-overlay.open{display:flex}
.modal{background:#ffffff;border-radius:12px;padding:20px;width:400px;max-width:90vw;border:0.5px solid #d3d1c7}
.modal-title{font-size:15px;font-weight:500;color:#1a1a18;margin-bottom:4px}
.modal-sub{font-size:12px;color:#888780;margin-bottom:16px}
.form-group{margin-bottom:12px}
.form-label{font-size:12px;color:#5f5e5a;margin-bottom:4px;display:block;font-weight:500}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.form-input{width:100%;padding:7px 10px;border:0.5px solid #d3d1c7;border-radius:8px;font-size:13px;color:#1a1a18;background:#f5f4f0;outline:none;font-family:inherit}
.form-input:focus{border-color:#1D9E75;background:#ffffff}
.form-select{width:100%;padding:7px 10px;border:0.5px solid #d3d1c7;border-radius:8px;font-size:13px;color:#1a1a18;background:#f5f4f0;outline:none;font-family:inherit;cursor:pointer}
.modal-actions{display:flex;gap:8px;justify-content:flex-end;margin-top:16px;padding-top:12px;border-top:0.5px solid #ebebE6}
.btn-cancel{padding:7px 14px;border-radius:8px;border:0.5px solid #d3d1c7;background:#ffffff;color:#5f5e5a;font-size:12px;cursor:pointer}
.btn-save{padding:7px 14px;border-radius:8px;border:none;background:#1D9E75;color:#ffffff;font-size:12px;cursor:pointer;font-weight:500}
.btn-save:hover{background:#0F6E56}
.toast{position:fixed;bottom:24px;right:24px;background:#1a1a18;color:#ffffff;padding:10px 16px;border-radius:8px;font-size:13px;opacity:0;transition:opacity 0.3s;z-index:200;pointer-events:none}
.toast.show{opacity:1}
.sidebar-footer{margin-top:auto;padding:12px 16px;border-top:0.5px solid #d3d1c7}
</style>
</head>
<body>

<div class="app">
  <!-- Sidebar -->
  <div class="sidebar">
    <div class="sidebar-header">
      <div class="app-logo"><span class="dot"></span>CareWatch</div>
      <div class="app-subtitle">Elder health monitoring</div>
    </div>
    <div class="nav-item active"><i class="ti ti-layout-dashboard"></i>Dashboard</div>
    <div class="nav-item"><i class="ti ti-users"></i>All patients</div>
    <div class="nav-item"><i class="ti ti-calendar"></i>Appointments</div>
    <div class="nav-item"><i class="ti ti-activity"></i>Vitals log</div>
    <div class="nav-item"><i class="ti ti-pill"></i>Medications</div>
    <div class="nav-item"><i class="ti ti-bell"></i>Alerts <span style="margin-left:auto;background:#FCEBEB;color:#791F1F;font-size:10px;padding:1px 6px;border-radius:20px">3</span></div>
    <div class="nav-section">Patients</div>
    <div class="patient-mini selected"><div class="avatar green">MH</div><span class="mini-name">Margaret Hall</span><span class="mini-status status-ok"></span></div>
    <div class="patient-mini"><div class="avatar blue">RN</div><span class="mini-name">Robert Nguyen</span><span class="mini-status status-warn"></span></div>
    <div class="patient-mini"><div class="avatar amber">EW</div><span class="mini-name">Edna Wallace</span><span class="mini-status status-alert"></span></div>
    <div class="patient-mini"><div class="avatar coral">JD</div><span class="mini-name">James Dolan</span><span class="mini-status status-ok"></span></div>
    <div class="patient-mini"><div class="avatar purple">SR</div><span class="mini-name">Sylvia Reeves</span><span class="mini-status status-ok"></span></div>
    <div class="sidebar-footer">
      <div class="nav-item" style="padding:6px 0"><i class="ti ti-settings"></i>Settings</div>
    </div>
  </div>

  <!-- Main -->
  <div class="main">
    <div class="topbar">
      <div class="topbar-left">
        <span class="page-title">Today's overview</span>
        <span class="date-badge" id="today-date"></span>
      </div>
      <div class="topbar-right">
        <div class="icon-btn"><i class="ti ti-search"></i></div>
        <div class="icon-btn"><i class="ti ti-bell"></i></div>
        <div class="avatar green" style="width:30px;height:30px;font-size:11px;cursor:pointer">NS</div>
      </div>
    </div>

    <div class="content">
      <!-- Stats -->
      <div class="summary-row">
        <div class="stat-card good">
          <div class="stat-label"><i class="ti ti-users"></i>Total patients</div>
          <div class="stat-value">5</div>
          <div class="stat-sub">4 stable · 1 critical</div>
        </div>
        <div class="stat-card warn">
          <div class="stat-label"><i class="ti ti-bell"></i>Active alerts</div>
          <div class="stat-value">3</div>
          <div class="stat-sub">2 high BP · 1 missed dose</div>
        </div>
        <div class="stat-card">
          <div class="stat-label"><i class="ti ti-calendar"></i>Check-ins today</div>
          <div class="stat-value">12</div>
          <div class="stat-sub">3 remaining</div>
        </div>
        <div class="stat-card good">
          <div class="stat-label"><i class="ti ti-pill"></i>Meds compliance</div>
          <div class="stat-value">87%</div>
          <div class="stat-sub">This week</div>
        </div>
      </div>

      <!-- Two-col layout -->
      <div class="two-col">
        <div style="display:flex;flex-direction:column;gap:14px">
          <div>
            <div class="section-header">
              <span class="section-title">Patients</span>
              <div style="display:flex;gap:8px;align-items:center">
                <button class="add-btn" onclick="openModal()"><i class="ti ti-plus"></i>Add patient</button>
                <span class="section-link">View all</span>
              </div>
            </div>
            <div class="patients-grid">
              <div class="patient-card selected">
                <div class="pc-header">
                  <div class="pc-avatar avatar green">MH</div>
                  <div class="pc-info"><div class="pc-name">Margaret Hall</div><div class="pc-meta">78 yrs · Room 12A</div></div>
                  <span class="pc-status-badge badge-ok">Stable</span>
                </div>
                <div class="vitals-row">
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-heart" style="color:#E24B4A"></i></div><div class="vital-val">72 bpm</div><div class="vital-lbl">Heart rate</div></div>
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-activity" style="color:#185FA5"></i></div><div class="vital-val">118/76</div><div class="vital-lbl">BP</div></div>
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-droplet" style="color:#1D9E75"></i></div><div class="vital-val">98%</div><div class="vital-lbl">SpO₂</div></div>
                </div>
              </div>
              <div class="patient-card">
                <div class="pc-header">
                  <div class="pc-avatar avatar blue">RN</div>
                  <div class="pc-info"><div class="pc-name">Robert Nguyen</div><div class="pc-meta">83 yrs · Room 7B</div></div>
                  <span class="pc-status-badge badge-warn">Monitor</span>
                </div>
                <div class="vitals-row">
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-heart" style="color:#E24B4A"></i></div><div class="vital-val">88 bpm</div><div class="vital-lbl">Heart rate</div></div>
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-activity" style="color:#BA7517"></i></div><div class="vital-val">148/92</div><div class="vital-lbl">BP</div></div>
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-droplet" style="color:#1D9E75"></i></div><div class="vital-val">96%</div><div class="vital-lbl">SpO₂</div></div>
                </div>
              </div>
              <div class="patient-card">
                <div class="pc-header">
                  <div class="pc-avatar avatar amber">EW</div>
                  <div class="pc-info"><div class="pc-name">Edna Wallace</div><div class="pc-meta">91 yrs · Room 3C</div></div>
                  <span class="pc-status-badge badge-alert">Critical</span>
                </div>
                <div class="vitals-row">
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-heart" style="color:#A32D2D"></i></div><div class="vital-val">104 bpm</div><div class="vital-lbl">Heart rate</div></div>
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-activity" style="color:#A32D2D"></i></div><div class="vital-val">162/99</div><div class="vital-lbl">BP</div></div>
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-droplet" style="color:#854F0B"></i></div><div class="vital-val">93%</div><div class="vital-lbl">SpO₂</div></div>
                </div>
              </div>
              <div class="patient-card">
                <div class="pc-header">
                  <div class="pc-avatar avatar coral">JD</div>
                  <div class="pc-info"><div class="pc-name">James Dolan</div><div class="pc-meta">74 yrs · Room 15A</div></div>
                  <span class="pc-status-badge badge-ok">Stable</span>
                </div>
                <div class="vitals-row">
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-heart" style="color:#E24B4A"></i></div><div class="vital-val">68 bpm</div><div class="vital-lbl">Heart rate</div></div>
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-activity" style="color:#185FA5"></i></div><div class="vital-val">122/80</div><div class="vital-lbl">BP</div></div>
                  <div class="vital-item"><div class="vital-icon"><i class="ti ti-droplet" style="color:#1D9E75"></i></div><div class="vital-val">99%</div><div class="vital-lbl">SpO₂</div></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Side panel -->
        <div class="side-panel">
          <div class="detail-card">
            <div class="detail-header">
              <div class="detail-avatar avatar green">MH</div>
              <div>
                <div class="detail-name">Margaret Hall</div>
                <div class="detail-meta">78 yrs · Diabetes, Hypertension</div>
              </div>
            </div>
            <div style="font-size:11px;color:#888780;margin-bottom:8px">Last check-in: 09:40 AM</div>
            <div class="vitals-detail">
              <div class="vd-item vd-normal"><div class="vd-top"><i class="ti ti-heart vd-icon"></i><span class="vd-label">Heart rate</span></div><div class="vd-value">72 bpm</div><div class="vd-range">Normal 60–100</div></div>
              <div class="vd-item vd-normal"><div class="vd-top"><i class="ti ti-activity vd-icon"></i><span class="vd-label">Blood pressure</span></div><div class="vd-value">118/76</div><div class="vd-range">Target &lt;130/80</div></div>
              <div class="vd-item vd-normal"><div class="vd-top"><i class="ti ti-droplet vd-icon"></i><span class="vd-label">SpO₂</span></div><div class="vd-value">98%</div><div class="vd-range">Normal ≥95%</div></div>
              <div class="vd-item vd-warn"><div class="vd-top"><i class="ti ti-thermometer vd-icon"></i><span class="vd-label">Temperature</span></div><div class="vd-value">37.8°C</div><div class="vd-range">Slightly elevated</div></div>
              <div class="vd-item vd-normal"><div class="vd-top"><i class="ti ti-droplet-half-2 vd-icon"></i><span class="vd-label">Blood glucose</span></div><div class="vd-value">6.4 mmol</div><div class="vd-range">Target 4–7</div></div>
              <div class="vd-item vd-normal"><div class="vd-top"><i class="ti ti-lungs vd-icon"></i><span class="vd-label">Resp. rate</span></div><div class="vd-value">16/min</div><div class="vd-range">Normal 12–20</div></div>
            </div>
            <button class="log-btn" onclick="openLogModal()">Log new vitals</button>
          </div>
          <div class="detail-card">
            <div class="section-header" style="margin-bottom:6px"><span class="section-title">Recent activity</span></div>
            <div class="activity-list" id="activity-list">
              <div class="activity-item"><div class="act-dot" style="background:#1D9E75"></div><div><div class="act-text">Vitals logged by Nurse Singh</div><div class="act-time">09:40 AM</div></div></div>
              <div class="activity-item"><div class="act-dot" style="background:#1D9E75"></div><div><div class="act-text">Morning medication taken — Metformin 500mg</div><div class="act-time">08:15 AM</div></div></div>
              <div class="activity-item"><div class="act-dot" style="background:#EF9F27"></div><div><div class="act-text">Temperature elevated — 37.8°C, flagged for review</div><div class="act-time">08:00 AM</div></div></div>
              <div class="activity-item"><div class="act-dot" style="background:#1D9E75"></div><div><div class="act-text">Breakfast completed, appetite good</div><div class="act-time">07:30 AM</div></div></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Add Patient Modal -->
<div class="modal-overlay" id="add-modal">
  <div class="modal">
    <div class="modal-title">Add new patient</div>
    <div class="modal-sub">Fill in the details to register a new patient.</div>
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">First name</label>
        <input class="form-input" id="f-fname" placeholder="e.g. Dorothy" type="text"/>
      </div>
      <div class="form-group">
        <label class="form-label">Last name</label>
        <input class="form-input" id="f-lname" placeholder="e.g. Smith" type="text"/>
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Age</label>
        <input class="form-input" id="f-age" placeholder="e.g. 76" type="number" min="60" max="120"/>
      </div>
      <div class="form-group">
        <label class="form-label">Room</label>
        <input class="form-input" id="f-room" placeholder="e.g. 9B" type="text"/>
      </div>
    </div>
    <div class="form-group">
      <label class="form-label">Primary conditions</label>
      <input class="form-input" id="f-conds" placeholder="e.g. Hypertension, Arthritis" type="text"/>
    </div>
    <div class="form-group">
      <label class="form-label">Status</label>
      <select class="form-select" id="f-status">
        <option value="stable">Stable</option>
        <option value="monitor">Monitor</option>
        <option value="critical">Critical</option>
      </select>
    </div>
    <div id="add-error" style="font-size:12px;color:#A32D2D;display:none;margin-top:4px"></div>
    <div class="modal-actions">
      <button class="btn-cancel" onclick="closeModal()">Cancel</button>
      <button class="btn-save" onclick="savePatient()">Add patient</button>
    </div>
  </div>
</div>

<!-- Log Vitals Modal -->
<div class="modal-overlay" id="log-modal">
  <div class="modal">
    <div class="modal-title">Log vitals — Margaret Hall</div>
    <div class="modal-sub">Record the latest readings. Leave blank to skip.</div>
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Heart rate (bpm)</label>
        <input class="form-input" id="v-hr" placeholder="e.g. 72" type="number"/>
      </div>
      <div class="form-group">
        <label class="form-label">SpO₂ (%)</label>
        <input class="form-input" id="v-spo2" placeholder="e.g. 98" type="number"/>
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Systolic BP</label>
        <input class="form-input" id="v-sys" placeholder="e.g. 118" type="number"/>
      </div>
      <div class="form-group">
        <label class="form-label">Diastolic BP</label>
        <input class="form-input" id="v-dia" placeholder="e.g. 76" type="number"/>
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Temperature (°C)</label>
        <input class="form-input" id="v-temp" placeholder="e.g. 37.2" type="number" step="0.1"/>
      </div>
      <div class="form-group">
        <label class="form-label">Blood glucose (mmol)</label>
        <input class="form-input" id="v-gluc" placeholder="e.g. 6.4" type="number" step="0.1"/>
      </div>
    </div>
    <div id="log-error" style="font-size:12px;color:#A32D2D;display:none;margin-top:4px"></div>
    <div class="modal-actions">
      <button class="btn-cancel" onclick="closeLogModal()">Cancel</button>
      <button class="btn-save" onclick="saveVitals()">Save vitals</button>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
  const colors = ['green','blue','amber','coral','purple'];
  let colorIdx = 0;

  function today() {
    return new Date().toLocaleDateString('en-GB',{weekday:'short',day:'numeric',month:'short',year:'numeric'});
  }
  document.getElementById('today-date').textContent = today();

  function openModal(){ document.getElementById('add-modal').classList.add('open'); }
  function closeModal(){ document.getElementById('add-modal').classList.remove('open'); document.getElementById('add-error').style.display='none'; }
  function openLogModal(){ document.getElementById('log-modal').classList.add('open'); }
  function closeLogModal(){ document.getElementById('log-modal').classList.remove('open'); document.getElementById('log-error').style.display='none'; }

  function showToast(msg){
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(()=>t.classList.remove('show'), 3000);
  }

  function savePatient(){
    const fname = document.getElementById('f-fname').value.trim();
    const lname = document.getElementById('f-lname').value.trim();
    const age = document.getElementById('f-age').value.trim();
    const room = document.getElementById('f-room').value.trim();
    const err = document.getElementById('add-error');
    if(!fname || !lname){ err.textContent='Enter first and last name.'; err.style.display='block'; return; }
    if(!age){ err.textContent='Enter the patient\'s age.'; err.style.display='block'; return; }
    err.style.display='none';
    const initials = (fname[0]+lname[0]).toUpperCase();
    const color = colors[colorIdx % colors.length]; colorIdx++;
    const status = document.getElementById('f-status').value;
    const badgeClass = status==='stable'?'badge-ok':status==='monitor'?'badge-warn':'badge-alert';
    const badgeLabel = status==='stable'?'Stable':status==='monitor'?'Monitor':'Critical';
    const dotClass = status==='stable'?'status-ok':status==='monitor'?'status-warn':'status-alert';
    // Add to sidebar
    const sidebar = document.querySelector('.sidebar-footer');
    const mini = document.createElement('div');
    mini.className='patient-mini';
    mini.innerHTML=`<div class="avatar ${color}">${initials}</div><span class="mini-name">${fname} ${lname}</span><span class="mini-status ${dotClass}"></span>`;
    sidebar.parentNode.insertBefore(mini, sidebar);
    // Add card
    const grid = document.querySelector('.patients-grid');
    const card = document.createElement('div');
    card.className='patient-card';
    card.innerHTML=`<div class="pc-header"><div class="pc-avatar avatar ${color}">${initials}</div><div class="pc-info"><div class="pc-name">${fname} ${lname}</div><div class="pc-meta">${age} yrs · Room ${room||'—'}</div></div><span class="pc-status-badge ${badgeClass}">${badgeLabel}</span></div><div class="vitals-row"><div class="vital-item"><div class="vital-icon"><i class="ti ti-heart" style="color:#E24B4A"></i></div><div class="vital-val">—</div><div class="vital-lbl">Heart rate</div></div><div class="vital-item"><div class="vital-icon"><i class="ti ti-activity" style="color:#888780"></i></div><div class="vital-val">—/—</div><div class="vital-lbl">BP</div></div><div class="vital-item"><div class="vital-icon"><i class="ti ti-droplet" style="color:#888780"></i></div><div class="vital-val">—%</div><div class="vital-lbl">SpO₂</div></div></div>`;
    grid.appendChild(card);
    closeModal();
    ['f-fname','f-lname','f-age','f-room','f-conds'].forEach(id=>document.getElementById(id).value='');
    document.getElementById('f-status').value='stable';
    showToast(`${fname} ${lname} added successfully`);
  }

  function saveVitals(){
    const hr = document.getElementById('v-hr').value;
    const spo2 = document.getElementById('v-spo2').value;
    const sys = document.getElementById('v-sys').value;
    const dia = document.getElementById('v-dia').value;
    const err = document.getElementById('log-error');
    if(!hr && !spo2 && !sys && !dia){ err.textContent='Enter at least one reading.'; err.style.display='block'; return; }
    err.style.display='none';
    const now = new Date().toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit'});
    const parts = [];
    if(hr) parts.push(`HR ${hr} bpm`);
    if(sys && dia) parts.push(`BP ${sys}/${dia}`);
    if(spo2) parts.push(`SpO₂ ${spo2}%`);
    const list = document.getElementById('activity-list');
    const item = document.createElement('div');
    item.className='activity-item';
    item.innerHTML=`<div class="act-dot" style="background:#1D9E75"></div><div><div class="act-text">Vitals logged — ${parts.join(', ')}</div><div class="act-time">${now}</div></div>`;
    list.insertBefore(item, list.firstChild);
    closeLogModal();
    ['v-hr','v-spo2','v-sys','v-dia','v-temp','v-gluc'].forEach(id=>document.getElementById(id).value='');
    showToast('Vitals saved successfully');
  }

  document.getElementById('add-modal').addEventListener('click',function(e){ if(e.target===this) closeModal(); });
  document.getElementById('log-modal').addEventListener('click',function(e){ if(e.target===this) closeLogModal(); });
</script>
</body>
</html>
"""

components.html(HTML, height=900, scrolling=True)
