# Architecture

```
┌───────────────────────────┐                                       ┌───────────────────────────┐
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │             globaltopic1              │                           │
│                           │                                       │                           │
│                           │──────────────────────────────────────▶│                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │             globaltopic2              │                           │
│         PiSender1         │                                       │         PiReceiver1       │
│                           │──────────────────────────────────────▶│                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │             globaltopic3              │                           │
│                           │                                       │                           │
│                           │──────────────────────────────────────▶│                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
│                           │                                       │                           │
└───────────────────────────┘                                       └───────────────────────────┘
```
