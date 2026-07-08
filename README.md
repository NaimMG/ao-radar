# AO Radar 🎯

**Intelligence sur les appels d'offres publics français, pour les PME et indépendants.**

## Le problème

Chaque année, l'État français publie des dizaines de milliers d'appels d'offres publics (BOAMP, marchés publics locaux). Pour une PME, un artisan ou un freelance, ce marché est presque inaccessible :

- **Découverte** : difficile de trouver les AO pertinents pour son activité au milieu du bruit
- **Compréhension** : un AO fait souvent 100-200 pages de jargon juridico-administratif
- **Décision** : difficile d'évaluer rapidement ses chances réelles de gagner
- **Réponse** : le dossier de candidature est complexe, avec de nombreuses pièces à ne pas oublier

Résultat : la commande publique reste largement inaccessible aux petites structures, alors qu'elle représente ~8% du PIB français.

## La solution — AO Radar

Une plateforme qui utilise le RAG et les LLM pour :

1. **Découvrir** — matcher automatiquement les AO pertinents selon le profil de l'entreprise
2. **Comprendre** — résumer un AO de 200 pages en synthèse actionnable (objet, critères, délais, montant)
3. **Évaluer** — scorer ses chances selon la taille du marché, la concurrence probable, l'historique du secteur
4. **Préparer** — générer une checklist guidée des pièces à fournir

## Architecture

\`\`\`
BOAMP API + data.gouv.fr (collecte des AO)
        ↓
Pipeline d'ingestion (nettoyage, structuration)
        ↓
ChromaDB (embeddings des documents AO)
        ↓
RAG + LLM (Groq llama-3.3-70b, fallback Ollama local)
        ↓
FastAPI Backend
        ↓
Next.js + TailwindCSS Frontend
        ↓
Supabase (authentification + historique utilisateur)
\`\`\`

| Couche | Technologie |
|---|---|
| Données | BOAMP API, data.gouv.fr |
| Embeddings | sentence-transformers (local) |
| Vector DB | ChromaDB |
| LLM | Groq (llama-3.3-70b) + Ollama fallback |
| Backend | FastAPI |
| Frontend | Next.js + TailwindCSS |
| Auth / DB | Supabase |
| Déploiement | Render (backend) + Vercel (frontend) |

## Statut du projet

🚧 En construction active — développé en public, étape par étape.

- [x] Cadrage produit et architecture
- [ ] Pipeline d'ingestion BOAMP
- [ ] Indexation vectorielle (ChromaDB)
- [ ] RAG + résumé automatique d'AO
- [ ] Scoring de pertinence / chances
- [ ] API backend (FastAPI)
- [ ] Interface web (Next.js)
- [ ] Authentification (Supabase)
- [ ] Déploiement production

## Auteur

Développé par [Naim](https://github.com/NaimMG) — dans le cadre d'un portfolio de projets Data/IA appliqués.
Autres projets : MLOps Pipeline, AgentFlow, PharmaRAG, DefectVision, AeroLLM, RailSafe, Maritime Route Optimizer, RecSys Realtime.