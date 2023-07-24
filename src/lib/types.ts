export type Status = {
  entities: Entities;
  created_at: string;
  in_reply_to_id: string;
  author_id: string;
  id: string;
  parsed_content: string;
  url: string;
};

export type StatusTuple = [string, Status[]];

export type GroupedStatuses = {
  [key: string]: Status[];
};

export type Entities = {
  hashtags?: Hashtag[];
  urls?: StatusUrl[];
  annotations?: StatusAnnotation[]; // TODO: deletable?
  day_list?: HdocDay[];
  modern_day_list?: ModernHdocDay[];
  src_list?: Src[];
  demo_list?: Demo[];
};

export type Hashtag = {
  start: number;
  end: number;
  tag: string;
};

export type StatusUrl = {
  start: number;
  end: number;
  url: string;
  expanded_url: string;
  display_url: string;
};

export type StatusAnnotation = {
  start: number;
  end: number;
  probability: number;
  type: string;
  normalized_text: string;
};

export type CustomEntityBase = {
  start: number;
  end: number;
};

export type HdocDay = CustomEntityBase & {
  day: string;
};

export type ModernHdocDay = CustomEntityBase & {
  day: string;
};

export type Src = CustomEntityBase & {
  src: string;
  fixed: boolean;
};

export type Demo = CustomEntityBase & {
  demo: string;
  fixed: boolean;
};

export type ExpandedEntity = {
  href: string;
  fixed: boolean;
};

export type ExpandedEntities = {
  demo: ExpandedEntity;
  src: ExpandedEntity;
};

export type ListBoxItem = {
  value: string;
  text: string;
};
