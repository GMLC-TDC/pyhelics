# Architecture

```
┌───────────────────────────┐                                       ┌───────────────────────────┐
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │             globaltopic1              │                           │
│         PiSender1         │                                       │         PiReceiver1       │
│                           │──────────────────────────────────────▶│                           │
│                           │                                       │                           │
│                           │                                   ┐   │                           │
│                           │    ╲                             ╱    │                           │
│                           │                                       │                           │
│                           │      ╲                         ╱      │                           │
│                           │                                       │                           │
│                           │        ╲                     ╱        │                           │
│                           │                                       │                           │
│                           │          ╲                 ╱          │                           │
│                           │           ┘                           │                           │
│                           │            ┌─────────────┐            │                           │
│                           │            │             │            │                           │
│                           │            │   Broker    │            │                           │
│                           │            │             │            │                           │
│                           │            └─────────────┘            │                           │
└───────────────────────────┘                                       └───────────────────────────┘
```
