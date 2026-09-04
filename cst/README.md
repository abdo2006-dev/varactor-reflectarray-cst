# CST project files

This directory holds documentation about the CST models. It does not hold the
models themselves.

## Why the .cst files are not committed

A CST Studio Suite project is a directory tree, not a single file. Alongside the
model it carries solver caches, tetrahedral mesh data, per-pass adaptive results,
field monitor dumps and automatic backups. A single converged run of this unit
cell can produce hundreds of megabytes, most of it regenerable. Committing that
into Git would make the repository unusable within a few branches and would gain
nothing that the parameter table in Appendix A does not already give.

The `.gitignore` therefore excludes `*.cst`, `Result/`, `Model/`, mesh and field
dumps, and CST backup files.

## How checkpoints are handled instead

Every model branch gets a versioned checkpoint file stored outside the
repository, on the machine running CST. The naming convention encodes the stage,
the source design, the CST version, the branch and the capacitance state.

```
CST_02_Harz2022_StageB_2023_v017_SourceTopology_C0025pF.cst
```

Rules that apply to those files:

1. A converged endpoint file is never overwritten. A new capacitance state or a
   new geometry gets a new file.
2. A checkpoint is saved before any structural change, so that a Boolean
   operation that replays badly can be rolled back rather than repaired.
3. Every branch named in `docs/experiment_log.md` has a corresponding
   checkpoint. The log is the index into the checkpoint set.

## What is committed instead

The parameter table in `report/sections/99_appendices.md`, Appendix A, and the
solver configuration in Appendix B are sufficient to rebuild the model. Together
with `docs/experiment_log.md` they define which branch produced which result.

Exported numerical results belong in `results/`, not here.

## If a .cst file ever needs to be committed

Use Git LFS, and commit only a single clean model checkpoint with its results
deleted, not a solved project directory.

```bash
git lfs install
git lfs track "*.cst"
git add .gitattributes
```

Before doing so, check the licence terms of the CST installation. Do not commit
licensed solver components, and do not commit any model that embeds third-party
material that is not the project's to redistribute.
