/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: cllc.proto */

#ifndef PROTOBUF_C_cllc_2eproto__INCLUDED
#define PROTOBUF_C_cllc_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1000000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1002001 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif

#include "api_mac.pb-c.h"

typedef struct _CllcAssociatedDevices CllcAssociatedDevices;
typedef struct _CllcStatistics CllcStatistics;


/* --- enums --- */

/*
 *!
 *Coordinator State Values
 */
typedef enum _CllcStates {
  /*
   *! Powered up, not started and waiting for user to start 
   */
  CLLC_STATES__Cllc_states_initWaiting = 1,
  /*
   *! Starting coordinator, scanning and selecting the best parameters 
   */
  CLLC_STATES__Cllc_states_startingCoordinator = 2,
  /*
   *!
   *Powered up, found network information, and restoring device in network
   */
  CLLC_STATES__Cllc_states_initRestoringCoordinator = 3,
  /*
   *! Device is operating as coordinator 
   */
  CLLC_STATES__Cllc_states_started = 4,
  /*
   *! Device is restored as coordinator in the network 
   */
  CLLC_STATES__Cllc_states_restored = 5,
  /*
   *! Joining allowed state has changed to allowed 
   */
  CLLC_STATES__Cllc_states_joiningAllowed = 6,
  /*
   *! Joining allowed state has changed to not allowed 
   */
  CLLC_STATES__Cllc_states_joiningNotAllowed = 7
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(CLLC_STATES)
} CllcStates;
/*
 *!
 *Coordinator starting State Values
 */
typedef enum _CllcCoordStates {
  /*
   *! Initialized state 
   */
  CLLC_COORD_STATES__Cllc_coordStates_initialized = 0,
  /*
   *! MAC  coordinator is performing a active scan  
   */
  CLLC_COORD_STATES__Cllc_coordStates_scanActive = 1,
  /*
   *! active scan  confirm received
   */
  CLLC_COORD_STATES__Cllc_coordStates_scanActiveCnf = 2,
  /*
   *! Eneergy detect scan confirm received 
   */
  CLLC_COORD_STATES__Cllc_coordStates_scanEdCnf = 3,
  /*
   *! Start confirm received 
   */
  CLLC_COORD_STATES__Cllc_coordStates_startCnf = 4
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(CLLC_COORD_STATES)
} CllcCoordStates;

/* --- messages --- */

/*
 *! Building block for association table 
 */
struct  _CllcAssociatedDevices
{
  ProtobufCMessage base;
  /*
   *! Short address of associated device 
   */
  uint32_t shortaddr;
  /*
   *! capability information 
   */
  ApiMacCapabilityInfo *capinfo;
  /*
   *! RSSI 
   */
  int32_t rssi;
  /*
   *! Device alive status 
   */
  uint32_t status;
};
#define CLLC_ASSOCIATED_DEVICES__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&cllc_associated_devices__descriptor) \
    , 0, NULL, 0, 0 }


/*
 *! Cllc statistics 
 */
struct  _CllcStatistics
{
  ProtobufCMessage base;
  /*
   *! number of PA Solicit messages received 
   */
  uint32_t fhnumpasolicitreceived;
  /*
   *! number of PA messages sent 
   */
  uint32_t fhnumpasent;
  /*
   *! number of PC Solicit messages received 
   */
  uint32_t fhnumpanconfigsolicitsreceived;
  /*
   *! number of PC messages sent 
   */
  uint32_t fhnumpanconfigsent;
  uint32_t otherstats;
};
#define CLLC_STATISTICS__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&cllc_statistics__descriptor) \
    , 0, 0, 0, 0, 0 }


/* CllcAssociatedDevices methods */
void   cllc_associated_devices__init
                     (CllcAssociatedDevices         *message);
size_t cllc_associated_devices__get_packed_size
                     (const CllcAssociatedDevices   *message);
size_t cllc_associated_devices__pack
                     (const CllcAssociatedDevices   *message,
                      uint8_t             *out);
size_t cllc_associated_devices__pack_to_buffer
                     (const CllcAssociatedDevices   *message,
                      ProtobufCBuffer     *buffer);
CllcAssociatedDevices *
       cllc_associated_devices__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   cllc_associated_devices__free_unpacked
                     (CllcAssociatedDevices *message,
                      ProtobufCAllocator *allocator);
/* CllcStatistics methods */
void   cllc_statistics__init
                     (CllcStatistics         *message);
size_t cllc_statistics__get_packed_size
                     (const CllcStatistics   *message);
size_t cllc_statistics__pack
                     (const CllcStatistics   *message,
                      uint8_t             *out);
size_t cllc_statistics__pack_to_buffer
                     (const CllcStatistics   *message,
                      ProtobufCBuffer     *buffer);
CllcStatistics *
       cllc_statistics__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   cllc_statistics__free_unpacked
                     (CllcStatistics *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*CllcAssociatedDevices_Closure)
                 (const CllcAssociatedDevices *message,
                  void *closure_data);
typedef void (*CllcStatistics_Closure)
                 (const CllcStatistics *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCEnumDescriptor    cllc_states__descriptor;
extern const ProtobufCEnumDescriptor    cllc_coord_states__descriptor;
extern const ProtobufCMessageDescriptor cllc_associated_devices__descriptor;
extern const ProtobufCMessageDescriptor cllc_statistics__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_cllc_2eproto__INCLUDED */
