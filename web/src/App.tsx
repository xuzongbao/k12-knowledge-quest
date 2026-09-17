import { useEffect, useMemo, useState } from "react";
import { getMap, listMaps } from "./catalog";
import { mapXpEarned } from "./engine";
import { loadProgress, saveProgress } from "./storage";
import type { PlayerProgress } from "./types";
import Home from "./views/Home";
import MapView from "./views/MapView";
import NodeView from "./views/NodeView";

interface Route {
  mapId?: string;
  nodeId?: string;
}

function parseHash(hash: string): Route {
  const raw = hash.replace(/^#/, "").replace(/^\/+/, "");
  const parts = raw.split("/").filter(Boolean);
  if (parts[0] === "m" && parts[1]) {
    return { mapId: decodeURIComponent(parts[1]), nodeId: parts[2] === "n" && parts[3] ? decodeURIComponent(parts[3]) : undefined };
  }
  return {};
}

function go(route: Route): void {
  if (!route.mapId) {
    location.hash = "#/";
    return;
  }
  const mapPart = `/m/${encodeURIComponent(route.mapId)}`;
  const nodePart = route.nodeId ? `/n/${encodeURIComponent(route.nodeId)}` : "";
  location.hash = `#${mapPart}${nodePart}`;
}

export default function App() {
  const [route, setRoute] = useState<Route>(() => parseHash(location.hash));
  const [progress, setProgress] = useState<PlayerProgress>(() => loadProgress());
  const [toast, setToast] = useState<string | null>(null);
  const [celebrate, setCelebrate] = useState<string | null>(null);

  useEffect(() => {
    const onHash = () => setRoute(parseHash(location.hash));
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, []);

  useEffect(() => {
    saveProgress(progress);
  }, [progress]);

  useEffect(() => {
    if (!toast) return;
    const t = window.setTimeout(() => setToast(null), 2600);
    return () => window.clearTimeout(t);
  }, [toast]);

  const maps = useMemo(() => listMaps(), []);
  const currentMap = route.mapId ? getMap(route.mapId) : undefined;

  const headerXp = currentMap ? mapXpEarned(currentMap, progress) : progress.xp_total;

  return (
    <div className="app-shell">
      <header className="topbar">
        <a className="brand" href="#/" onClick={(e) => { e.preventDefault(); go({}); }}>
          <span className="brand-mark" aria-hidden>
            灯
          </span>
          <div>
            <h1>知识探险</h1>
            <p>点亮知识点，打关升级</p>
          </div>
        </a>
        <div className="xp-pill" title="累计经验">
          经验 {currentMap ? `${headerXp}（本图）` : progress.xp_total}
        </div>
      </header>

      {!route.mapId && (
        <Home
          maps={maps}
          progress={progress}
          onOpenMap={(id) => go({ mapId: id })}
        />
      )}

      {route.mapId && !currentMap && (
        <p className="empty">找不到这张地图。请回到首页再选一次。</p>
      )}

      {currentMap && !route.nodeId && (
        <MapView
          map={currentMap}
          progress={progress}
          onBack={() => go({})}
          onOpenNode={(nodeId) => go({ mapId: currentMap.meta.id, nodeId })}
          onBlocked={(msg) => setToast(msg)}
          onReset={(next) => {
            setProgress(next);
            setToast("本图进度已清空。");
          }}
        />
      )}

      {currentMap && route.nodeId && (
        <NodeView
          map={currentMap}
          nodeId={route.nodeId}
          progress={progress}
          onBack={() => go({ mapId: currentMap.meta.id })}
          onProgress={(next, note) => {
            setProgress(next);
            if (note.mapJustCleared) {
              setCelebrate(currentMap.meta.title);
            } else if (note.nodeJustLit) {
              setToast("灯亮了！后面的知识点可能已经解锁。");
            } else if (note.blockedReason) {
              setToast(note.blockedReason);
            }
          }}
        />
      )}

      {toast && <div className="toast" role="status">{toast}</div>}

      {celebrate && (
        <div className="modal-backdrop" role="dialog" aria-labelledby="win-title">
          <div className="modal">
            <h2 id="win-title">通关啦！</h2>
            <p>你点亮了「{celebrate}」的全部知识点，并击败了关主。</p>
            <button className="primary" type="button" onClick={() => setCelebrate(null)}>
              继续探险
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
